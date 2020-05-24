from __future__ import division
import glob
from ROOT import *
DY17dir=glob.glob('/eos/uscms/store/group/lpchbb/LLDJntuples/2017_LLDJ/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DY50_1_amcW2/190705_140540/0000/*')
DY16dir=glob.glob('/eos/uscms/store/group/lpchbb/LLDJntuples/topRWT/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_DY50_1/180928_181036/0000/*')

sample='DY50'   
h16 = TH1F("h16",'%s AODCaloJet AM 16vs17' % sample,50, 0, 1)
hT16 = TH1F("hT16",'%s AODCaloJet AM 16vs17vs17w/weight' % sample,50, 0, 1)
h17 = TH1F("h17",'%s GenMatch<0.95 AM' % sample,50, 0, 1)
hT17 = TH1F("hT17",'%s GenMatch<0.95 AM' % sample,50, 0, 1)
hPU16 = TH1F("hPU16",'%s AOD 16,17 MC AODnTruePU' % sample,80, 0, 80)
hPU17 = TH1F("hPU17",'%s AOD 17 MC AODnTruePU' % sample,80, 0, 80)
hPUratio = TH1F("hPUratio",'%s AOD 16/17 MC AODnTruePU' % sample,80, 0, 80)

for i in range (100):
        filename = DY16dir[i]
	_file0 = TFile.Open(filename,'read')
	#myfile = TFile.Open(_file0)
	mytree16 = _file0.Get("lldjNtuple/EventTree")
	for entry in mytree16:
		nTruePU = mytree16.AODnTruePU
		hPU16.Fill(nTruePU,1)
	_file0.Close()
for i in range (100):
        filename = DY17dir[i]
	_file0 = TFile.Open(filename,'read')
	#myfile = TFile.Open(_file0)
	mytree17 = _file0.Get("lldjNtuple/EventTree")
	for entry in mytree17:
		nTruePU=mytree17.AODnTruePU
		hPU17.Fill(nTruePU,1)
	_file0.Close()
c2 = TCanvas( 'c2', 'Histogram Drawing Options', 200, 10, 700, 900 )
hPU16.SetLineColor(3)
hPU16.Draw('e1')
#hPU16.Scale(1./hPU16.Integral())
hPU17.SetLineColor(4)
hPU17.Draw('e1 SAME')
#hPU17.Scale(1./hPU17.Integral())
c2.Modified()
c2.Update()
#c2.SaveAs('AOD16PUQCD.png')
c4 = TCanvas( 'c4', 'Histogram Drawing Options', 200, 10, 700, 900 )
hPUratio =hPU16.Clone("hPUratio")
hPUratio.SetTitle('%s AOD 16/17 MC AODnTruePU' % sample)
hPUratio.Divide(hPU17)
hPUratio.Draw('e1')
c4.Modified()
c4.Update()
#c4.SaveAs('AODratioPUQCD.png')
_file1 = TFile.Open('new.root', "recreate")
hPU17.Write()
hPUratio.Write()
_file1.Close()



for i in range (100):
        filename = DY16dir[i]
	_file0 = TFile.Open(filename,'read')
	mytree16 = _file0.Get("lldjNtuple/EventTree")
	for entry in mytree16:
		#weight=mytree16.AODGenEventWeight
 		alphamax = mytree16.AODCaloJetAlphaMax
		for flow in alphamax:
			h16.Fill(flow,1)
			#hnlo16.Fill(flow,1)
			#hTnlo16.Fill(flow,weight)
	_file0.Close()
for i in range (100):
        filename = DY17dir[i]
	_file0 = TFile.Open(filename,'read')
	mytree17 = _file0.Get("lldjNtuple/EventTree")
	for entry in mytree17:
		truePU = mytree17.AODnTruePU
   		puscale = hPUratio.GetBinContent(truePU)
		#weight=mytree17.AODGenEventWeight
		alphamax = mytree17.AODCaloJetAlphaMax
		for flow in alphamax:
			#puweight = 0
			h17.Fill(flow,puscale)
			#puweight = weight
			#puweight *= puscale
			hT17.Fill(flow,1)
	_file0.Close()
#gPad.SetLogy()
c1 = TCanvas( 'c1', 'Histogram Drawing Options', 200, 10, 700, 900 )
h16.Draw('HIST')
h16.SetLineColor(3)
factor16=h16.Integral()
h17.Draw('HIST SAME')
h17.SetLineColor(6)
factor17 = h17.Integral()
scale17 = factor16/factor17
h17.Scale(scale17)
hT17.Draw('HIST SAME')
hT17.SetLineColor(7)
factor17T = hT17.Integral()
scale17T = factor16/factor17T
hT17.Scale(scale17T)
legend2 = TLegend(0.2,0.60,0.4,0.85) 		
legend2.SetTextSize(0.015)
legend2.AddEntry(h16,"#splitline{2016 madgraph}{unitary weight}","f")
legend2.AddEntry(h17,"#splitline{2017 amcatnlo}{unitary weight w/pileup}","f")
legend2.AddEntry(hT17,"#splitline{2017 amcatnlo}{GenEventInfo w/opileup}","f")
legend2.Draw()

c1.Modified()
c1.Update()
c1.SaveAs('AODratioQCD.png')
k=raw_input('Press ENTER to exit')
