from __future__ import division
from ROOT import *
import glob
import math
gROOT.ForceStyle(kTRUE)

c1 = TCanvas( 'c1', 'Histogram Drawing Options', 200, 10, 700, 900 )
gPad.SetTickx()
gPad.SetTicky()
gStyle.SetOptStat(0)
gStyle.SetLineWidth(3)
gStyle.SetHistLineWidth(3)
gPad.SetLeftMargin(0.12)
gPad.SetBottomMargin(0.12)
higgs = '150'
llp = '50'

#_file0 = TFile.Open('/uscms/home/ddiaz/nobackup/ZDark_LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/h125_llp20_ct100_mc_AOD.root','read')
_file0 = TFile.Open('/uscms/home/ddiaz/nobackup/ZDark_LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/h150_llp20_ct100_100k_mc_AOD.root','read')
_file1 = TFile.Open('/uscms/home/ddiaz/nobackup/ZDark_LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/h175_llp20_ct100_100k_mc_AOD.root','read')
#_file0 = TFile.Open('/uscms/home/ddiaz/nobackup/ZDark_LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/h175_llp50_ct100_100k_mc_AOD.root','read')
_file2 = TFile.Open('/uscms/home/ddiaz/nobackup/ZDark_LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/h200_llp20_ct100_100k_mc_AOD.root','read')
#_file0 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/h200_llp50_ct100_100k_mc_AOD.root','read')

#ISRdir=glob.glob('/eos/uscms/store/group/lpchbb/LLDJntuples/topRWT/h125_llp20_ct100_100k_wISR/crab_h125_llp20_ct100_100k_wISR/200319_210825/0000/*')
#ISRdir=glob.glob('/eos/uscms/store/group/lpchbb/LLDJntuples/topRWT/h150_llp20_ct100_100k_wISR/crab_h150_llp20_ct100_100k_wISR/200319_212718/0000/*')
#_file0 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/ntuples/config/lldjntuple_mc_h150_llp50_ct100.root','read')
#_file1 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/ntuples/config/lldjntuple_mc_h175_llp50_ct100.root','read')
#_file2 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/ntuples/config/lldjntuple_mc_h200_llp50_ct100.root','read')
#ISRdir=glob.glob('/eos/uscms/store/group/lpchbb/LLDJntuples/topRWT/h175_llp20_ct100_100k_wISR/crab_h175_llp20_ct100_100k_wISR/200319_214501/0000/*')
#ISRdir=glob.glob('/eos/uscms/store/group/lpchbb/LLDJntuples/topRWT/h175_llp50_ct100_100k_wISR/crab_h175_llp50_ct100_100k_wISR/200320_143608/0000/*')
#ISRdir=glob.glob('/eos/uscms/store/group/lpchbb/LLDJntuples/topRWT/h200_llp20_ct100_100k_wISR/crab_h200_llp20_ct100_100k_wISR/200319_215151/0000/*')
#ISRdir=glob.glob('/eos/uscms/store/group/lpchbb/LLDJntuples/topRWT/h200_llp50_ct100_100k_wISR/crab_h200_llp50_ct100_100k_wISR/200319_215853/0000/*')
hnoISR = TH1F("h_150",'',60, 0, 1.2)
hISR = TH1F("h_175",'',60, 0, 1.2)
hISR2 = TH1F("h_200",'',60, 0, 1.2)
llp0 = _file0.Get("lldjNtuple/EventTree")
for entry in llp0:
	daughter=llp0.AODCaloJetAlphaMax
	for pt in daughter:
		hnoISR.Fill(pt,1)
llp1 = _file1.Get("lldjNtuple/EventTree")
for entry in llp1:
	daughter=llp1.AODCaloJetAlphaMax
	for pt in daughter:
		hISR.Fill(pt,1)
llp2 = _file2.Get("lldjNtuple/EventTree")
for entry in llp2:
	daughter=llp2.AODCaloJetAlphaMax
	for pt in daughter:
		hISR2.Fill(pt,1)
#for i in range (len(ISRdir)):
#        filename = ISRdir[i]
#	_file1 = TFile.Open(filename,'read')
#	llp1 = _file1.Get("lldjNtuple/EventTree")
#	for entry in llp1:
#		daughter=llp1.Zpt
#		for pt in daughter:
#			hISR.Fill(pt,1)
#	_file1.Close()
#for entry in llp2:
#	daughter=llp2.Zpt
#	for pt in daughter:
#		SdR2.Fill(pt,1)
hnoISR.GetXaxis().SetTitle("GenLevel-TA")
hnoISR.GetYaxis().SetTitle("Events")
hnoISR.GetYaxis().SetTitleOffset(1.5)
hnoISR.Scale(1/hnoISR.Integral())
hnoISR.SetLineColor(1)
hnoISR.Draw("HIST")
hnoISR.GetYaxis().SetRangeUser(0,.2)
hISR.Scale(1/hISR.Integral())
hISR.SetLineColor(3)
hISR.Draw("HIST SAME")
hISR2.Scale(1/hISR2.Integral())
hISR2.SetLineColor(4)
hISR2.Draw("HIST SAME")
#SdR2.Scale(1/SdR2.Integral())
#SdR2.SetLineColor(2)
#SdR2.Draw("HIST SAME")
legend = TLegend(0.55,0.65,0.85,0.85) 		
legend.SetTextSize(0.022)
legend.SetBorderSize(0)
legend.SetNColumns(2)
legend.SetFillColor(kWhite)
legend.AddEntry(hnoISR,"#splitline{h150_llp20_}{ct100}","l")
legend.AddEntry(hISR,"#splitline{h175_llp20_}{ct100}","l")
legend.AddEntry(hISR2,"#splitline{h200_llp20_}{ct100}","l")
#legend.AddEntry(SdR2,"#splitline{h150_llp20_}{ct100_ISR}","l")
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
extra2.SetTextSize(0.025)
extra2.SetTextColor(kBlack)
extra2.SetTextAlign(11)
extra2.SetTextFont(62)
title.DrawTextNDC(0.2,0.91,"CMS")
extra.DrawTextNDC(0.3,0.91,"Preliminary")
extra2.DrawLatexNDC(0.55,0.91,"Run2 Zdark")
c1.Modified()
c1.Update()
c1.SaveAs("Zdark_AMnoISR.png")
#_file2 = TFile.Open('h%s_llp%s.root'%(higgs,llp), "recreate")
#hISR.Write()
#hnoISR.Write()
#_file2.Close()

k=raw_input('Press ENTER to exit')
