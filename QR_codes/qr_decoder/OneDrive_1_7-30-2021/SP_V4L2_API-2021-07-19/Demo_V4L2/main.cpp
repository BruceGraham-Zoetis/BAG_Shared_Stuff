/*
 * main.c -- Sunplus IT camera SDK demo (V4L2)
 *
 * 			2018 Frank Chang, SunplusIT
 * 
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <getopt.h>
#include <time.h>
#include <errno.h>
#include "../include/sunpluscamera.h"

enum { 
	OP_UNKNOWN,
	OP_BACKEND_READ,
	OP_BACKEND_WRITE,
	OP_SENSOR_READ,
	OP_SENSOR_WRITE,
	OP_UPLOAD_SECTOR,
	OP_DOWNLOAD_SECTOR,
	OP_UPLOAD_FW,
	OP_DOWNLOAD_FW,
};

void MyProgressCB(unsigned int progress)
{
	printf("\x8\x8\x8\x8");		
	printf("%3d%%", progress);
	fflush(stdout); 
}

unsigned long long ahextoui64(const char* String)
{
	unsigned long length=(unsigned long)strlen(String);
	unsigned long long ret=0;
	if (length>8)
	{	return 0x10000;}
	else
	{
		unsigned long i=0;
		for (i=0;i<length;i++)
		{
			switch (String[i])
			{
			case '0':
				ret+=((0)<<((length-i-1)*4));
				break;
			case '1':
				ret+=((1)<<((length-i-1)*4));
				break;
			case '2':
				ret+=((2)<<((length-i-1)*4));
				break;
			case '3':
				ret+=((3)<<((length-i-1)*4));
				break;
			case '4':
				ret+=((4)<<((length-i-1)*4));
				break;
			case '5':
				ret+=((5)<<((length-i-1)*4));
				break;
			case '6':
				ret+=((6)<<((length-i-1)*4));
				break;
			case '7':
				ret+=((7)<<((length-i-1)*4));
				break;
			case '8':
				ret+=((8)<<((length-i-1)*4));
				break;
			case '9':
				ret+=((9)<<((length-i-1)*4));
				break;
			case 'a':
				ret+=((10)<<((length-i-1)*4));
				break;
			case 'b':
				ret+=((11)<<((length-i-1)*4));
				break;
			case 'c':
				ret+=((12)<<((length-i-1)*4));
				break;
			case 'd':
				ret+=((13)<<((length-i-1)*4));
				break;
			case 'e':
				ret+=((14)<<((length-i-1)*4));
				break;
			case 'f':
				ret+=((15)<<((length-i-1)*4));
				break;
			case 'A':
				ret+=((10)<<((length-i-1)*4));
				break;
			case 'B':
				ret+=((11)<<((length-i-1)*4));
				break;
			case 'C':
				ret+=((12)<<((length-i-1)*4));
				break;
			case 'D':
				ret+=((13)<<((length-i-1)*4));
				break;
			case 'E':
				ret+=((14)<<((length-i-1)*4));
				break;
			case 'F':
				ret+=((15)<<((length-i-1)*4));
				break;
			case ' ':
				break;
			case 0:
				break;
			default:
				return 0x10001;
			}
		}
	}
	return ret;
}

void usage(const char *argv0)
{
	fprintf(stderr, "Usage: sudo %s\t [OPTION]...\n\n%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s",
		 argv0,
		 " Initial device (1): \n",
		 "\t-V, --vid\ttarget device vid\n",
		 "\t-P, --pid\ttarget device pid\n",
		 " Initial device (2): \n",
		 "\t-D, --device\ttarget device number ( /dev/video# )\n\n",
		 "\t-u, --update\tDownload FW\n",
		 "\t-d, --dump\t\tDump FW from device\n",
		 " Backend register : \n",
		 "\t-r, --reg-read\t\tRead register\n",
		 "\t\trequire : <address>\n",
		 "\t-w, --reg-write\t\tWrite register\n",
		 "\t\trequire : <address> <value>\n",
		 "\t-a, --address\t\tAddress (hex)\n",
		 "\t-e, --value\t\tValue (hex)\n",
		"\t-n, --up-sector\t\tupload sector\n",
		"\t\trequire : <sector>\n",
		"\t-m, --dl-sector\t\twrite sector\n",
		"\t\trequire : <sector>\n"
	);
}

int GetTargetDeviceNode(unsigned short vid, unsigned short pid)
{
    int theIndex = -1;
    for(int i=0; i<10; i++)
    {
	FILE *pf = NULL;
	char szDevPath[260]; memset(szDevPath, 0, 260);
	char szTemp[260]; memset(szTemp, 0, 260);
	sprintf(szDevPath, "/sys/class/video4linux/video%d/device/uevent", i);
	pf = fopen(szDevPath, "r");
	if(pf == NULL)
	{
	//    printf("Cannot open : %s\n\tErrorNO: %d\n", szDevPath, errno);
	    continue;
	}
	
	char szLine[260]; memset(szLine, 0, 260);
	char *szVid = NULL, *szPid = NULL, *szBcd = NULL;
	unsigned short tmpVID = 0;
	unsigned short tmpPID = 0;
	while(fgets(szLine, 260, pf) != NULL)
	{
	    // get a line up to 260 chars. done if NULL
	    strcpy(szTemp, szLine);
	    if(strcasestr(szTemp, "PRODUCT") != NULL)
	    {
		//DEBUG(szTemp);
		szVid = strtok(szTemp, "=");
		szVid = strtok(NULL, "/");
		szPid = strtok(NULL, "/");
		szBcd = strtok(NULL, "/");
		break;
	    }
	}
	tmpVID = strtol(szVid, NULL, 16);
	tmpPID = strtol(szPid, NULL, 16);
	fclose(pf);
	//printf("Find device : 0x%X, 0x%X\n", tmpVID, tmpPID);
	if(tmpVID == vid && tmpPID == pid)
	{
	    theIndex = i;
	    break;
	}
	else
	{
	//    printf("not match, next.\n");
	}
    }
    return theIndex;
}

int main(int argc, char *argv[])
{ 
    int retCode = 0;

	int c;
	unsigned char flashType, icType;
	int helpflag = 0;
	const char* szAddr = 0;
	const char* szValue = 0;

	FILE *pf = NULL;
	char szFWFile[260];
	unsigned char *downloadFirmwareCode = NULL;
	unsigned char *uploadFirmwareCode = NULL;
	unsigned char sectorCode[0x1000];
	unsigned long ulBufferSize = 0;

	unsigned short answer = 0;
	int addr = -1;
	unsigned char val;
	unsigned short usVID = 0;
	unsigned short usPID = 0;
	
	int sector = 0;
	int cmd = OP_UNKNOWN;
	char devNode[100];

	unsigned long ulFlashSize = 0;
	unsigned char cID[5];
	memset(cID, 0, 5);

	memset(devNode, 0, 100);

	memset(sectorCode, 0, 0x1000);
	srand(time(0));
	
	if (argc < 3) {
		usage(argv[0]);
		return 1;
	}
	
	struct option longopts[] = 
	{
		//const char *name, int has_arg, *flag, int val
		{"device", 				1, 0, 'D'},
		{"vid",					1, 0, 'V'},
		{"pid",					1, 0, 'P'},
		{"update",		 		1, 0, 'u'},
		{"dump", 		 		0, 0, 'd'},
		{"reg-write",		 	0, 0, 'w'},
		{"reg-read",		 	0, 0, 'r'},
		{"sen-reg-write",	 	0, 0, 'x'},
		{"sen-reg-read",	 	0, 0, 'y'},
		{"address",		 		1, 0, 'a'},
		{"value",		 		1, 0, 'e'},
		{"up-sector",		 	1, 0, 'n'},
		{"dl-sector",		 	1, 0, 'm'},
		{"help", 		 		0, &helpflag, 1},
		{0, 0, 0, 0}
	};

	SunplusCamera *pCamera = NULL;
	
	while ((c = getopt_long(argc, argv, "D:wa:re:u:dxyn:m:V:P:", longopts, NULL)) != EOF)
	{
		switch(c)
		{
			case 'V':
			    usVID = strtol(optarg, NULL, 16);
			    break;
			case 'P':
			    usPID = strtol(optarg, NULL, 16);
			    break;
			case 'D':
				sprintf(devNode, "/dev/video%s", optarg);
				break;
			break;
			case 'u':
				printf("Command: Download FW\n");
				cmd = OP_DOWNLOAD_FW;
				memset(szFWFile, 0, 260);
				strcpy(szFWFile, optarg);
				break;
			case 'd':
				printf("Command: Upload FW\n");
				cmd = OP_UPLOAD_FW;
				break;
			case 'a':
				szAddr = optarg;
				break;
			case 'e':
				szValue = optarg;
				break;
			case 'w':
				printf("Command: write sensor register\n");
				cmd = OP_BACKEND_WRITE;
				break;
			case 'r':
				printf("Command: read backend register\n");
				cmd = OP_BACKEND_READ;
				break;
			case 'x':
				printf("Command: write sensor register\n");
				cmd = OP_SENSOR_WRITE;
				break;
			case 'y':
				printf("Command: read sensor register\n");
				cmd = OP_SENSOR_READ;
				break;
			case 'n':
				printf("Command: Upload data from sector\n");
				sector = atoi(optarg);
				cmd = OP_UPLOAD_SECTOR;
				break;
			case 'm':
				printf("Command: Write data to sector\n");
				sector = atoi(optarg);
				cmd = OP_DOWNLOAD_SECTOR;
				break;
			default:
				break;
		}
	}

	// initial camera device
	if(usVID != 0 && usPID != 0)
	{
	    int idx = GetTargetDeviceNode(usVID , usPID);
	    if(idx == -1)
	    {
		printf("%d:%d not found.\n", usVID, usPID);
		return 1;
	    }
	    sprintf(devNode, "/dev/video%d", idx);
	}
	pCamera = new SunplusCamera();
	printf("open device : %s\n", devNode);
	retCode = pCamera->SunplusCamera_Init(devNode);
	
	if(retCode != 0)
	{
		printf("SunplusCamera init fail.\n");
		return 1;
	}
	
	//printf("SunplusCamera init ok.\n");

	// try to get flash type
	//printf("Read Flash.\n");
	pCamera->Get_FlashType (&flashType);
	pCamera->Get_FlashSize(flashType, &ulFlashSize);
	pCamera->Get_FlashID(0x9F, cID);
	pCamera->Get_ASICType (&icType);
	printf("IC TYPE : %d, Flash Type : %d\n", icType, flashType);
	printf("Flash ID: 0x%X, 0x%X, 0x%X\nFlash Size: 0x%X (%d)\n",
		cID[0], cID[1], cID[2], ulFlashSize, ulFlashSize);
	switch(cmd)	
	{
		case OP_DOWNLOAD_FW:
			if(flashType == SF_UNDEFINED){
				printf("flash type is not supported...\n");
				goto uninit;
			}
			
			// load binary
			pf = fopen(szFWFile, "rb");
			if(pf == NULL)
			{
				retCode = 2;
				printf("open %s fail\n", szFWFile);
				goto uninit;
			}

			// read fw buffer
			fseek(pf, 0, SEEK_END);
			ulBufferSize = ftell(pf);
			fseek(pf, 0, SEEK_SET);

			// allocate buffer
			downloadFirmwareCode = (unsigned char*)malloc(ulBufferSize);
			memset(downloadFirmwareCode, 0, ulBufferSize);
			fread(downloadFirmwareCode, 1, ulBufferSize, pf);
			printf("Binary file : [%s] %lu bytes (%.1f KB) has been read\n",
			       szFWFile, ulBufferSize, ulBufferSize/1024.0);
			
			printf("Start update firmware..\n");
			retCode = pCamera->Download_FW (downloadFirmwareCode, ulBufferSize, flashType,
			                      NULL, NULL, NULL, &MyProgressCB);
			if(retCode == 0)
				printf("\nDownload finished(%d)\n", retCode);
			else
				printf("\nDownload failed(%d)\n", retCode);
			goto uninit;
		break;
		case OP_UPLOAD_FW:
			if(flashType == SF_UNDEFINED){
				printf("flash type is not supported.\n");
				goto uninit;
			}
			
			// allocate buffer
			retCode = pCamera->Get_FlashSize(flashType, &ulBufferSize);
			if(retCode != 0)
			    ulBufferSize = 0x10000;
			uploadFirmwareCode = (unsigned char*)malloc(ulBufferSize);
			retCode = pCamera->Upload_FW (uploadFirmwareCode, flashType, ulBufferSize, &MyProgressCB);
			if(retCode==0)
			{
				FILE *p = NULL;
				p = fopen("dump.bin", "wb");
				if(p == NULL)
				{
					retCode = 1;
					printf("cannot open dump.bin\n");
					fclose(pf);
					goto uninit;
				}

				fwrite(uploadFirmwareCode, 1, ulBufferSize, p);
				fclose(p);
				printf("Upload_FW finished, save to dump.bin\n");
			}
			else
			{
				printf("Upload_FW fail\n");
			}
			goto uninit;
		break;
		case OP_UPLOAD_SECTOR:
			printf("Read Data : \n\t");
			if(flashType == SF_UNDEFINED){
			    printf("flash type is not supported..\n");
				goto uninit;
			}
			retCode = pCamera->Upload_Sector (sectorCode, sector, flashType);
			if(retCode)
			{
				printf("Upload_Sector fail.\n");
				goto uninit;
			}
			else
			{
				printf("read sector %d data : \n", sector);
				for(int i=0; i<128; i++)
				{
					if(i > 0)
					{
						if(i%15 == 0)
							printf("\n");
						else
							printf(", ");
					}
					printf("0x%02X", sectorCode[i]);
				}
			}
			
			goto uninit;
		break;
		case OP_DOWNLOAD_SECTOR:
			printf("Write Data : \n\t");
			if(flashType == SF_UNDEFINED){
				printf("flash type is not supported..\n");
				goto uninit;
			}

			// dummy data
			for(int i=0; i<0x1024; i++)
			{
				sectorCode[i] = (unsigned char)(rand() & 0xFF);
			}
			retCode = pCamera->Write_Sector (sectorCode, sector, flashType);
			if(retCode)
			{
				printf("Write_Sector fail.\n");
			}
			else
			{
				printf("Write Sector ok\n");
			}
	
			goto uninit;
		break;
		case OP_BACKEND_WRITE:
			printf(" Command : Register Write\n");
			if(szAddr == NULL || szValue == NULL)
			{
				printf("  * need address and value\n\t\t %s -w -a <address> -e <value>\n\texample: %s -w -a 250d -e 1\n ", argv[0], argv[0]);
				goto uninit;
			}

			addr = (int)ahextoui64(szAddr);
		
			if(addr > 0xffff)
			{
				printf("\n  *Incorrect register address, its character can only be 0~9, a~f(A~F), its length can only <= 4\n");
				goto uninit;
			}
			
			val = (unsigned char)ahextoui64(szValue);
			if(val > 0xffff)
			{
				printf("\n  *Incorrect register value, its character can only be 0~9, a~f(A~F), its length can only <= 4\n");
				goto uninit;
			}
		
			retCode = pCamera->SetASICRegister (addr, val);
			if(retCode)
				printf(" Register Write fail.\n");
			else
				printf(" Register Write : 0x%X => 0x%X\n", addr, val);
		break;
		case OP_BACKEND_READ:
			printf(" Command : Register Read\n");
			if(szAddr == NULL)
			{
				printf("  * need address\n\t\t %s -r -a <address>\n\texample: %s -r -a 250d\n", argv[0], argv[0]);
				goto uninit;
			}
			addr = (int)ahextoui64(szAddr);
		
			if(addr > 0xffff)
			{
				printf("\n  *Incorrect register address, its character can only be 0~9, a~f(A~F), its length can only <= 4\n");
				goto uninit;
			}

			retCode = pCamera->GetASICRegister(addr, (unsigned char*)&answer);
			if(retCode)
				printf(" Register Read fail\n");
			else
				printf(" Register Read : 0x%X = 0x%X\n", addr, answer);
		break;
		case OP_SENSOR_WRITE:
			printf(" Command : Sensor Register Write\n");
			if(szAddr == NULL || szValue == NULL)
			{
				printf("  * need address and value\n\t\t %s -x -a <address> -e <value>\n\texample: %s -x -a 250d -e 1\n ", argv[0], argv[0]);
				goto uninit;
			}
			addr = (int)ahextoui64(szAddr);
		
			if(addr > 0xffff)
			{
				printf("\n  *Incorrect sensor register address, its character can only be 0~9, a~f(A~F), its length can only <= 4\n");
				goto uninit;
			}
			
			val = (unsigned short)ahextoui64(szValue);
			if(val > 0xffff)
			{
				printf("\n  *Incorrect sensor register value, its character can only be 0~9, a~f(A~F), its length can only <= 4\n");
				goto uninit;
			}

			retCode = pCamera->SetSensorRegister (addr, val);
			if(retCode)
				printf(" Sensor Register Write fail\n");
			else
				printf(" Sensor Register Write : 0x%X => 0x%X\n", addr, val);
		break;
		case OP_SENSOR_READ:
			printf(" Command : Sensor Register Read\n");
			if(szAddr == NULL)
			{
				printf("  * need address\n\t\t %s -y -a <address>\n\texample: %s -y -a 250d\n", argv[0], argv[0]);
				goto uninit;
			}
			addr = (int)ahextoui64(szAddr);
		
			if(addr > 0xffff)
			{
				printf("\n  *Incorrect sensor register address, its character can only be 0~9, a~f(A~F), its length can only <= 4\n");
				goto uninit;
			}
		
			retCode = pCamera->GetSensorRegister (addr, &answer);
			if(retCode)
				printf(" Sensor Register Read fail\n");
			else
				printf(" Sensor Register Read : 0x%X = 0x%X\n", addr, answer);
		break;
	}

uninit:
	printf("\nuninit...\n");
	if(pCamera)
		delete pCamera;
	if(pf)
		fclose(pf);
	if(downloadFirmwareCode)
		delete[] downloadFirmwareCode;
	if(uploadFirmwareCode)
		delete[] uploadFirmwareCode;
	
	printf("main end\n");
    return retCode;
}
