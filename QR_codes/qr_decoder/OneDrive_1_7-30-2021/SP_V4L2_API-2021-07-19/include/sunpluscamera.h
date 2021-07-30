#ifndef __SUNPLUSCAMERA_H__
#define __SUNPLUSCAMERA_H__

#if 0
#include <linux/videodev2.h>
#include <linux/uvcvideo.h>
#include <linux/usb/video.h>
#include <stdint.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/ioctl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#endif

#define MX			0
#define SST			1
#define PMC			2
#define EON			3
#define AMIC		4
#define ATM			5
#define MX_32Byte	6
#define SF_EXT		10
#define	MCM_Flash_EON	254
#define	MCM_Flash_SST	255

enum {
	NO_CAMERA = 0,
	CAMERA_ONLINE = 20,
	CAMERA_NOT_MATCH,

	DL_INITIAL,					//download complete percentage = 0%
	DL_LOOP_RUNNING,			//download complete percentage = 5%~95%
	DL_LOOP_FINISH,				//download complete percentage = 95%
	DL_COMPLETE,				//download complete percentage = 100%
	DL_WAITING,
	DL_ERROR,

	SPCA_UNKNOWNIC = 100,
	SPCA_2000BC,
	SPCA_2000D,
	SPCA_AllIC,
	SPCA_2080,
	SPCA_2088,
	SPCA_2082,
	SPCA_2085,
	SPCA_2089,
	SPCA_2610,
	SPCA_2650,
	SPCA_2720,
	SPCA_2120,
	SPCA_2050,
    SPCA_2150,

	SF_UNDEFINED = 0,

	// MX
	SF_MX25L512,
	SF_GD25Q512,
	SF_FM25F005,
	SF_FM25F01,
	SF_MD25D512,
	SF_MD25D10,
	SF_MX25L1006E,
	SF_GT25F512,
	SF_PM25LQ512,
	SF_W25X05CL,
	SF_MK25D40,
	SF_ZB25D16,
	SF_MK25D16,
	SF_GD25D10B,
	SF_BY25Q512,

	SF_MX25V1006F,
	SF_W25X10CL,

	SF_MK25D80,
	SF_MK25D40BT,
	SF_T25S80XZ,
	SF_P25Q40H,
	SF_T25S80PW,
	SF_P25Q05H,
	SF_P25Q10H,

	SF_MX25L4006E,
	SF_PM25WQ080,
	SF_PM25LQ080,
	SF_GD25LQ128,
	SF_GD25LQ80,
	SF_W25Q80BW,
	SF_GD25Q16C,
	SF_GD25Q20C,
	SF_LE25U20AMB,	

	SF_BG25Q40A,
	SF_GD25Q40C,
	SF_BH25D40A,
	SF_GD25D20C,
	SF_MX25L2006E,  
	SF_MX25V2033FM1L, // = MX25L2006E
	SF_P25Q21H,
	SF_FM25W04,
	SF_FM25Q04,
	SF_FM25W02,
	SF_MX25V2035F,
	SF_W25X40CLSNIG,
	SF_W25X20CLSNIG,
	SF_MX25U3235F, 
	SF_XT25F01,
	SF_XT25F01C_D,
	SF_BH25D05,	
	SF_BH25D10B,
	SF_MX25V8035F,
	SF_MX25L6406E,
	SF_FH25V08,
	SF_P25Q80H,
	SF_GD25Q80CTIG,
	SF_EN25Q80C,

	// MX32
	SF_MX25L5121E,
	SF_MX25L1021E,
	SF_KH25L5121E,
	SF_KH25L1021E,

	// SST
	SF_SST25VF512,

	// PMC
	SF_PM25LD512,
	SF_PM25LD256,
	SF_PM25LV512,

	// ATM
	SF_AT25F512B,

	// EON
	SF_EN25F05,
	SF_EN25F40,
	SF_EN25F10A,
	SF_EN25F20A,
	SF_EN25Q40A,

	// AMIC
	SF_AMICA25LS512,

	SF_RESERVED,

	SF_WriteProtect_UNDEFINED = 150,
	SF_WriteProtect_ON,
	SF_WriteProtect_OFF,

	SP_NOT_EXPECTED_ARGU = 160,

	CAMERA_NORMAL_TYPE = 200,
	CAMERA_SENSOR_TYPE,
	CAMERA_ALL_TYPE,
};

typedef void(*ProgressCB) (unsigned int progress);

class info_camera_os	//get information from system
{
public:
	unsigned short vid;
	unsigned short pid;
	unsigned short bcdDevice;
};

class info_camera_bin
{
public:
    unsigned short vid;
    unsigned short pid;
    unsigned short FWVersion;
    unsigned short FWsubVersion;
};

class SunplusCamera
{
public:
    SunplusCamera();
    ~SunplusCamera();

#ifdef LIBUSB_H
    int SunplusCamera_Init(libusb_device_handle *devh, unsigned char icType=SPCA_AllIC);
#else
    int SunplusCamera_Init(char* DEVNODE=(char*)"/dev/video0", unsigned char icType=SPCA_AllIC);
#endif
    
    int SunplusCamera_UnInit();

    char* GetVersion(); // get library version
	
    // Register
    int GetASICRegister(unsigned short addr, unsigned char* Reg_Value);
    int SetASICRegister(unsigned short addr, unsigned char Reg_Value);
    int GetSensorRegister(unsigned short addr, unsigned short* Sensor_Reg_Value);
    int SetSensorRegister(unsigned short addr, unsigned short Sensor_Reg_Value);
    int GetSensorRegister(unsigned char slaveID,unsigned short addr, unsigned short* Sensor_Reg_Value);
    int SetSensorRegister(unsigned char slaveID,unsigned short addr, unsigned short Sensor_Reg_Value);
    
    // get backend, flash type 
    int Get_ASICType(unsigned char* type);
    int Get_FlashType(unsigned char* type);
    int Get_FlashSize(unsigned char type, unsigned long* dwSize);
    int Get_FlashID(unsigned char addr, unsigned char *pID);
    
    int Get_information_OS(info_camera_os* info);
    int Get_information_BIN(info_camera_bin* info, unsigned char *FW, int length);
    // call this function before Download FW
    int PreReset();
    
    // serial flash read/writes
    int Download_FW(unsigned char *FW, unsigned long FW_Length, unsigned char FlashType, 
                    unsigned char* SW_chksum=NULL, unsigned char* FW_chksum=NULL,
                    unsigned char* status=NULL, ProgressCB pCB=NULL, 
                    bool eraseAll=false, bool reset=true);
    
    int Download_FW_MCM(unsigned char *FW, unsigned long FW_Length, unsigned char* SW_chksum=NULL, 
			unsigned char* FW_chksum=NULL, unsigned char* status=NULL, unsigned char* percent=NULL,
			ProgressCB pCB=NULL);
	
    int Upload_FW(unsigned char *FW, unsigned char FlashType, const unsigned long dwSize = 0x10000, ProgressCB pCB=NULL); // default 64KB
	
    int Write_Sector(unsigned char *FW, int index, unsigned char FlashType);
    int Upload_Sector(unsigned char *FW, int index, unsigned char FlashType);

    int SetSF_WProtect_ON(unsigned char FlashType);
    int SetSF_WProtect_OFF(unsigned char FlashType);
    
    int GetI2CRegister(unsigned char slaveID, unsigned short addr, unsigned char* buffer, unsigned int bufferLength);
    int SetI2CRegister(unsigned char slaveID, unsigned short addr, unsigned char* buffer, unsigned int bufferLength);
    
    int SetI2C(unsigned char* pValue, const unsigned long ulSize);
    int GetI2C(unsigned char* pValue, const unsigned long ulSize);

    int ReworkFW(unsigned char **FW, unsigned long FW_Length, unsigned char FlashType, unsigned char SNAddr);

    class pData;
    pData *hand;
	
};
#endif /* __SUNPLUSCAMERA_H__ */
