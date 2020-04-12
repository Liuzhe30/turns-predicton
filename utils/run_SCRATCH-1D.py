# -*- coding:utf-8 -*-
'''
	File Name：     run_SCRATCH-1D
	Description :   generate second structure features of fasta files
	Author :        Liu Zhe
	date：          2020/2/27
'''
import os
class SCRATCH():
    def runSCRATCH(self,fastapath,outpath):
        names = [name for name in os.listdir(fastapath) if os.path.isfile(os.path.join(fastapath + '//', name))]
        for each_item in names:
            pdb_id = each_item.split('.')[0]
            cmd = '/home/RaidDisk/liuzhe002/SCRATCH-1D/SCRATCH-1D_1.1/bin/run_SCRATCH-1D_predictors.sh '+ fastapath + '/' + each_item + ' ' + outpath + '/' + pdb_id + '.out 4'
            os.system(cmd)
      
      
if __name__ == '__main__':

    '''
    samples:
    fastapath = '/home/liuzhe002/HHblits/HHFasta'
    outpath = '/home/RaidDisk/liuzhe002/HHResult'
    You can also check the structure and format of used fasta files in my folder : /home/liuzhe002/HHblits/HHFasta
    Warning : the permissions issue has not been resolved, please use the filepath under /home/RaidDisk/ as your outpath
    '''
    
    fastapath = '/home/liuzhe002/3_beta_turn/BT6376_FASTA_5'
    outpath = '/home/RaidDisk/liuzhe002/3_beta_turn/BT6376_HHResults'
    
    hh = SCRATCH()
    hh.runSCRATCH(fastapath, outpath)