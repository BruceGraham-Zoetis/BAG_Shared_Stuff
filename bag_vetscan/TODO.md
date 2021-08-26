* analyzer_dracula
   finish adding calls to draculad to generated file.

	def measurement_supported_consumables_get():
	    oDracula = CDBusDraculaService()
	    strConsumables = oDracula.draculad.measurement_supported_consumables_get()
	    return strConsumables
   
* run copy_modified_files_to_templates.sh




