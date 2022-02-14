from __future__ import division
import glob
from ROOT import *
DY18dir=glob.glob('/eos/uscms/store/group/lpchbb/LLDJntuples/suhoRutgersWH/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/crab_QCD_Pt_120to170_2018/210411_032454/0000/*')

sample='DY50'   
hPU18 = TH1F("hPU18",'%s AOD 18 MC AODnTruePU' % sample,80, 0, 80)

for i in range (90):
        filename = DY18dir[i]
	_file0 = TFile.Open(filename,'read')
	#myfile = TFile.Open(_file0)
	mytree18 = _file0.Get("TreeMakerMINIAOD/HiggsLongLived")
	for entry in mytree18:
		nTruePU = mytree18.trueNumInteractions_
		print(nTruePU)
		hPU18.Fill(nTruePU)
	_file0.Close()
c2 = TCanvas( 'c2', 'Histogram Drawing Options', 200, 10, 700, 900 )
hPU18.SetLineColor(3)
hPU18.Draw('e1')
c2.Modified()
c2.Update()
_file1 = TFile.Open('new.root', "recreate")
hPU18.Write()
_file1.Close()
k=raw_input('Press ENTER to exit')
