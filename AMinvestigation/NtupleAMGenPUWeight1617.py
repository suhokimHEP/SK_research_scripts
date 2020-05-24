## \file
## \ingroup tutorial_pyroot
## \notebook -js
## A Simple histogram drawing example
##
## \macro_image
## \macro_output
## \macro_code
##
## \author Wim Lavrijsen
from __future__ import division
import glob
from ROOT import *
DY17dir=glob.glob('/eos/uscms/store/group/lpchbb/LLDJntuples/2017_LLDJ/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DY50_1_amcW2/190705_140540/0000/*')
DYnlo16dir=glob.glob('/eos/uscms/store/group/lpchbb/LLDJntuples/topRWT/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_DY50_amcW5/190711_172851/0000/*')
DY16dir=glob.glob('/eos/uscms/store/group/lpchbb/LLDJntuples/topRWT/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_DY50_1/180928_181036/0000/*')


c1 = TCanvas( 'c1', 'Histogram Drawing Options', 200, 10, 700, 900 )
gStyle.SetOptStat(0)
gPad.SetLeftMargin(0.13)
gPad.SetBottomMargin(0.12)
gPad.SetTopMargin(0.12)
gPad.SetTickx()
gPad.SetTicky()
gStyle.SetLineWidth(3)
gStyle.SetHistLineWidth(3)
sample='DY50'   
hnlo16 = TH1F("hnlo16",'%s AODCaloJet AM 16vs17' % sample,50, 0, 1)
hTnlo16 = TH1F("hnloT16",'%s AODCaloJet AM 16vs17vs17w/weight' % sample,50, 0, 1)
h17 = TH1F("h17",'%s GenMatch<0.95 AM' % sample,50, 0, 1)
hT17 = TH1F("hT17",'%s GenMatch<0.95 AM' % sample,50, 0, 1)
hPU16 = TH1F("hPU16",'%s MC 16,17 AODnTruePU' % sample,80, 0, 80)
hPU17 = TH1F("hPU17",'%s AOD 17 MC AODnTruePU' % sample,80, 0, 80)
hPUratio = TH1F("hPUratio",'%s AOD 16/17 MC AODnTruePU' % sample,80, 0, 80)

for i in range (50):
        filename = DYnlo16dir[i]
	_file0 = TFile.Open(filename,'read')
	#myfile = TFile.Open(_file0)
	mytree16 = _file0.Get("lldjNtuple/EventTree")
	for entry in mytree16:
		nTruePU = mytree16.AODnTruePU
		hPU16.Fill(nTruePU,1)
	_file0.Close()
for i in range (50):
        filename = DY17dir[i]
	_file0 = TFile.Open(filename,'read')
	#myfile = TFile.Open(_file0)
	mytree17 = _file0.Get("lldjNtuple/EventTree")
	for entry in mytree17:
		nTruePU=mytree17.AODnTruePU
		hPU17.Fill(nTruePU,1)
	_file0.Close()
hPU16.SetLineColor(1)
hPU17.SetLineColor(2)
hPU16.Scale(1./hPU16.Integral())
hPU16.GetXaxis().SetTitle("AODnTruePU")
hPU16.GetYaxis().SetTitle("Unit Normalized distribution")
hPU16.Draw('e1')
hPU17.Scale(1./hPU17.Integral())
hPU17.Draw('e1 SAME')
legend = TLegend(0.75,0.70,0.9,0.85) 		
legend.AddEntry(hPU16,"2016","f")
legend.AddEntry(hPU17,"2017","f")
legend.Draw()
title = TText(1,1,"") 
title.SetTextSize(0.045)
title.SetTextColor(kBlack)
title.SetTextAlign(11)
title.SetTextFont(62)

extra = TText(1,1,"") 
extra.SetTextSize(0.03)
extra.SetTextColor(kBlack)
extra.SetTextAlign(11)
extra.SetTextFont(52)

extra2 = TLatex(1,1,"") 
extra2.SetTextSize(0.03)
extra2.SetTextColor(kBlack)
extra2.SetTextAlign(11)
extra2.SetTextFont(42)
title.DrawTextNDC(0.20,0.90,"CMS")
extra.DrawTextNDC(0.3,0.90,"Preliminary")
c1.Modified()
c1.Update()
c1.SaveAs("PUdist.pdf")
c2 = TCanvas( 'c2', 'Histogram Drawing Options', 200, 10, 700, 900 )
gPad.SetLeftMargin(0.13)
gPad.SetBottomMargin(0.12)
gPad.SetTopMargin(0.12)
gPad.SetTickx()
gPad.SetTicky()
hPUratio =hPU16.Clone("hPUratio")
hPUratio.SetTitle('%s AOD 16/17 MC AODnTruePU' % sample)
hPUratio.GetXaxis().SetTitle('AODnTruePU')
hPUratio.GetYaxis().SetTitle('16/17 ratio')
hPUratio.Divide(hPU17)
hPUratio.Draw('e1')
title = TText(1,1,"") 
title.SetTextSize(0.045)
title.SetTextColor(kBlack)
title.SetTextAlign(11)
title.SetTextFont(62)

extra = TText(1,1,"") 
extra.SetTextSize(0.03)
extra.SetTextColor(kBlack)
extra.SetTextAlign(11)
extra.SetTextFont(52)

extra2 = TLatex(1,1,"") 
extra2.SetTextSize(0.03)
extra2.SetTextColor(kBlack)
extra2.SetTextAlign(11)
extra2.SetTextFont(42)
title.DrawTextNDC(0.20,0.90,"CMS")
extra.DrawTextNDC(0.3,0.90,"Preliminary")
c2.Modified()
c2.Update()
c2.SaveAs("PUratio.pdf")
#c4.SaveAs('AODratioPUQCD.png')
_file1 = TFile.Open('new.root', "recreate")
hPU16.Write()
hPU17.Write()
hPUratio.Write()
_file1.Close()
c3 = TCanvas( 'c3', 'Histogram Drawing Options', 200, 10, 700, 900 )
gPad.SetLeftMargin(0.13)
gPad.SetBottomMargin(0.12)
gPad.SetTopMargin(0.12)
gPad.SetTickx()
gPad.SetTicky()
	
for i in range (50):
        filename = DYnlo16dir[i]
	_file0 = TFile.Open(filename,'read')
	#myfile = TFile.Open(_file0)
	mytree16 = _file0.Get("lldjNtuple/EventTree")
	for entry in mytree16:
		weight=mytree16.AODGenEventWeight
 		alphamax = mytree16.AODCaloJetAlphaMax
		for flow in alphamax:
			hnlo16.Fill(flow,1)
			hTnlo16.Fill(flow,weight)
for i in range (50):
        filename = DY17dir[i]
	_file0 = TFile.Open(filename,'read')
	#myfile = TFile.Open(_file0)
	mytree17 = _file0.Get("lldjNtuple/EventTree")
	for entry in mytree17:
		truePU = mytree17.AODnTruePU
   		puscale = hPUratio.GetBinContent(truePU)
		weight=mytree17.AODGenEventWeight
		newweight = puscale*weight
		alphamax = mytree17.AODCaloJetAlphaMax
		for flow in alphamax:
			h17.Fill(flow,1)
			hT17.Fill(flow,newweight)
hnlo16.Draw('HIST')
hnlo16.Scale(1/hnlo16.Integral())
hnlo16.GetXaxis().SetTitle("AlphaMax")
hnlo16.SetLineColor(1)
factornlo16 = hnlo16.Integral()
h17.Draw('HIST SAME')
h17.SetLineColor(2)
factor17 = h17.Integral()
scale17 = factornlo16/factor17
h17.Scale(1/h17.Integral())
hT17.Draw('HIST SAME')
hT17.SetLineColor(3)
factor17T = hT17.Integral()
scale17T = factornlo16/factor17T
hT17.Scale(1/hT17.Integral())
legend2 = TLegend(0.2,0.60,0.4,0.86) 		
legend2.AddEntry(hnlo16,"2016 AlphaMax","f")
legend2.AddEntry(h17,"2017 AlphaMax","f")
legend2.AddEntry(hT17,"#splitline{2017 AlphaMax}{with 16/17 PUratio}","f")
legend2.Draw()
title = TText(1,1,"") 
title.SetTextSize(0.045)
title.SetTextColor(kBlack)
title.SetTextAlign(11)
title.SetTextFont(62)

extra = TText(1,1,"") 
extra.SetTextSize(0.03)
extra.SetTextColor(kBlack)
extra.SetTextAlign(11)
extra.SetTextFont(52)

extra2 = TLatex(1,1,"") 
extra2.SetTextSize(0.03)
extra2.SetTextColor(kBlack)
extra2.SetTextAlign(11)
extra2.SetTextFont(42)
title.DrawTextNDC(0.20,0.90,"CMS")
extra.DrawTextNDC(0.3,0.90,"Preliminary")
#extra2.DrawLatexNDC(0.55,0.89,"2016 lumi 16.2/fb (13 TeV)")

c3.Modified()
c3.Update()
c3.SaveAs('AM_16v17.pdf')
#c3.Modified()
#c3.Update()
#c3.SaveAs('AOD17PU.png')
k=raw_input('Press ENTER to exit')
