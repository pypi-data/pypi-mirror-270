#init funciton

from .gssurgo2soil import SOL

"""
    Converts gSSURGO format into DSSAT .SOL format.
    
    Inputs
    ------
        path: string
            path to your .csv file containing the data from gSSURGO. Must have the following columns(and other related depths)
            WC15Bar_DCP_0to5
            WC3rdbar_DCP_0to5
            Clay_DCP_0to5
            Silt_DCP_0to5
            pHwater_DCP_0to5
            CEC_DCP_0to5
            Db3rdbar_DCP_0to5
            Ksat_DCP_0to5
            OrgMatter_DCP_0to5
            MUKEY_DCP_0to5
        
        path2: string
            path where u want to save files
    Example:
    --------
            path = 'Username/pathtothecsv'
            path2 = 'Username/pathtosavingfolder'
            ssurgo2soil(path,path2)
            
"""