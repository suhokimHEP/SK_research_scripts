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
higgs = '125'
llp = '20'

_file0 = TFile.Open('/uscms/home/ddiaz/nobackup/ZDark_LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/h125_llp20_ct100_mc_AOD.root','read')
#_file0 = TFile.Open('/uscms/home/ddiaz/nobackup/ZDark_LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/h150_llp20_ct100_100k_mc_AOD.root','read')
#_file0 = TFile.Open('/uscms/home/ddiaz/nobackup/ZDark_LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/h150_llp50_ct100_100k_mc_AOD.root','read')
#_file0 = TFile.Open('/uscms/home/ddiaz/nobackup/ZDark_LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/h175_llp20_ct100_100k_mc_AOD.root','read')
#_file0 = TFile.Open('/uscms/home/ddiaz/nobackup/ZDark_LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/h175_llp50_ct100_100k_mc_AOD.root','read')
#_file0 = TFile.Open('/uscms/home/ddiaz/nobackup/ZDark_LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/h200_llp20_ct100_100k_mc_AOD.root','read')
#_file0 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/h200_llp50_ct100_100k_mc_AOD.root','read')

ISRdir=glob.glob('/eos/uscms/store/group/lpchbb/LLDJntuples/topRWT/h125_llp20_ct100_100k_wISR/crab_h125_llp20_ct100_100k_wISR/200319_210825/0000/*')
#ISRdir=glob.glob('/eos/uscms/store/group/lpchbb/LLDJntuples/topRWT/h150_llp20_ct100_100k_wISR/crab_h150_llp20_ct100_100k_wISR/200319_212718/0000/*')
#ISRdir=glob.glob('/eos/uscms/store/group/lpchbb/LLDJntuples/topRWT/h150_llp50_ct100_100k_wISR/crab_h150_llp50_ct100_100k_wISR/200319_213800/0000/*')
#ISRdir=glob.glob('/eos/uscms/store/group/lpchbb/LLDJntuples/topRWT/h175_llp20_ct100_100k_wISR/crab_h175_llp20_ct100_100k_wISR/200319_214501/0000/*')
#ISRdir=glob.glob('/eos/uscms/store/group/lpchbb/LLDJntuples/topRWT/h175_llp50_ct100_100k_wISR/crab_h175_llp50_ct100_100k_wISR/200320_143608/0000/*')
#ISRdir=glob.glob('/eos/uscms/store/group/lpchbb/LLDJntuples/topRWT/h200_llp20_ct100_100k_wISR/crab_h200_llp20_ct100_100k_wISR/200319_215151/0000/*')
#ISRdir=glob.glob('/eos/uscms/store/group/lpchbb/LLDJntuples/topRWT/h200_llp50_ct100_100k_wISR/crab_h200_llp50_ct100_100k_wISR/200319_215853/0000/*')
SdR0 = TH1F("Scalar_dR0",'',4, 0, 4)
SdR1 = TH1F("Scalar_dR1",'',4, 0, 4)
llp0 = _file0.Get("lldjNtuple/EventTree")
for entry in llp0:
	daughter=llp0.AODnCaloJet
	SdR0.Fill(daughter,1)
for i in range (len(ISRdir)):
        filename = ISRdir[i]
	_file1 = TFile.Open(filename,'read')
	llp1 = _file1.Get("lldjNtuple/EventTree")
	for entry in llp1:
		daughter=llp1.AODnCaloJet
		SdR1.Fill(daughter,1)
	_file1.Close()
#for entry in llp2:
#	daughter=llp2.Zpt
#	for pt in daughter:
#		SdR2.Fill(pt,1)
SdR0.GetXaxis().SetTitle("AODnCaloJet")
SdR0.GetYaxis().SetTitle("Events")
SdR0.GetYaxis().SetRangeUser(0,1)
SdR0.GetYaxis().SetTitleOffset(1.5)
SdR0.Scale(1/SdR0.Integral())
SdR0.SetLineColor(1)
SdR0.Draw("HIST")
SdR1.Scale(1/SdR1.Integral())
SdR1.SetLineColor(3)
SdR1.Draw("HIST SAME")
#SdR2.Scale(1/SdR2.Integral())
#SdR2.SetLineColor(2)
#SdR2.Draw("HIST SAME")
legend = TLegend(0.55,0.65,0.85,0.85) 		
legend.SetTextSize(0.022)
legend.SetBorderSize(0)
legend.SetNColumns(2)
legend.SetFillColor(kWhite)
legend.AddEntry(SdR0,"#splitline{h%s_llp%s_}{ct100}"%(higgs,llp),"l")
legend.AddEntry(SdR1,"#splitline{h%s_llp%s_}{ct100_combined}"%(higgs,llp),"l")
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
c1.SaveAs("Zdark_ZnJet%sllp%s.png"%(higgs,llp))

k=raw_input('Press ENTER to exit')
