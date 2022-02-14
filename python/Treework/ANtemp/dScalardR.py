from __future__ import division
from ROOT import *
gROOT.ForceStyle(kTRUE)

c1 = TCanvas( 'c1', 'Histogram Drawing Options', 200, 10, 700, 900 )
c1.SetGrid()
gPad.SetTickx()
gPad.SetTicky()
gStyle.SetOptStat(0)
gStyle.SetLineWidth(3)
gStyle.SetHistLineWidth(3)
gPad.SetLeftMargin(0.12)
gPad.SetBottomMargin(0.12)
_file0 = TFile.Open('/uscms/home/ddiaz/nobackup/ZDark_LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/h125_llp20_ct100_mc_AOD.root','read')
_file1 = TFile.Open('/uscms/home/ddiaz/nobackup/ZDark_LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/h150_llp20_ct100_100k_mc_AOD.root','read')
_file2 = TFile.Open('/uscms/home/ddiaz/nobackup/ZDark_LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/h175_llp20_ct100_100k_mc_AOD.root','read')
_file3 = TFile.Open('/uscms/home/ddiaz/nobackup/ZDark_LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/h200_llp20_ct100_100k_mc_AOD.root','read')
_file4 = TFile.Open('/uscms/home/ddiaz/nobackup/ZDark_LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/h250_llp20_ct100_mc_AOD.root','read')
_file5 = TFile.Open('/uscms/home/ddiaz/nobackup/ZDark_LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/h500_llp20_ct100_mc_AOD.root','read')
#_file6 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/topRWT/ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8/crab_ZH_HToSSTobbbb_MS-55_ctauS-100/181004_091330/0000/lldjntuple_mc_AOD_1.root','read')
llp0 = _file0.Get("lldjNtuple/EventTree")
SdR0 = TH1F("Scalar_dR0",'',30, 0, 5)
for entry in llp0:
	daughter_Eta=llp0.llpDaughterEta
	daughter_Phi=llp0.llpDaughterPhi
	dPhi = daughter_Phi[1]-daughter_Phi[0]
	if dPhi>3.14:	
		dPhi = 6.28-dPhi
	dR1 = ((daughter_Eta[1]-daughter_Eta[0])**2+dPhi**2)**.5 
	#dR2 = ((daughter_Eta[3]-daughter_Eta[2])**2+(daughter_Phi[3]-daughter_Phi[2])**2)**.5
	SdR0.Fill(dR1,1)
	#SdR0.Fill(dR2,1)
llp1 = _file1.Get("lldjNtuple/EventTree")
SdR1 = TH1F("Scalar_dR1",'',30, 0, 5)
for entry in llp1:
	daughter_Eta=llp1.llpDaughterEta
	daughter_Phi=llp1.llpDaughterPhi
	dPhi = daughter_Phi[1]-daughter_Phi[0]
	if dPhi>3.14:	
		dPhi = 6.28-dPhi
	dR1 = ((daughter_Eta[1]-daughter_Eta[0])**2+dPhi**2)**.5 
	#dR2 = ((daughter_Eta[3]-daughter_Eta[2])**2+(daughter_Phi[3]-daughter_Phi[2])**2)**.5 
	SdR1.Fill(dR1,1)
	#SdR1.Fill(dR2,1)
llp2 = _file2.Get("lldjNtuple/EventTree")
SdR2 = TH1F("Scalar_dR2",'',30, 0, 5)
for entry in llp2:
	daughter_Eta=llp2.llpDaughterEta
	daughter_Phi=llp2.llpDaughterPhi
	dPhi = daughter_Phi[1]-daughter_Phi[0]
	if dPhi>3.14:	
		dPhi = 6.28-dPhi
	dR1 = ((daughter_Eta[1]-daughter_Eta[0])**2+dPhi**2)**.5 
	#dR2 = ((daughter_Eta[3]-daughter_Eta[2])**2+(daughter_Phi[3]-daughter_Phi[2])**2)**.5 
	SdR2.Fill(dR1,1)
	#SdR2.Fill(dR2,1)
llp3 = _file3.Get("lldjNtuple/EventTree")
SdR3 = TH1F("Scalar_dR3",'',30, 0, 5)
for entry in llp3:
	daughter_Eta=llp3.llpDaughterEta
	daughter_Phi=llp3.llpDaughterPhi
	dPhi = daughter_Phi[1]-daughter_Phi[0]
	if dPhi>3.14:	
		dPhi = 6.28-dPhi
	dR1 = ((daughter_Eta[1]-daughter_Eta[0])**2+dPhi**2)**.5 
	#dR2 = ((daughter_Eta[3]-daughter_Eta[2])**2+(daughter_Phi[3]-daughter_Phi[2])**2)**.5 
	SdR3.Fill(dR1,1)
	#SdR3.Fill(dR2,1)
llp4 = _file4.Get("lldjNtuple/EventTree")
SdR4 = TH1F("Scalar_dR4",'',30, 0, 5)
for entry in llp4:
	daughter_Eta=llp4.llpDaughterEta
	daughter_Phi=llp4.llpDaughterPhi
	dPhi = daughter_Phi[1]-daughter_Phi[0]
	if dPhi>3.14:	
		dPhi = 6.28-dPhi
	dR1 = ((daughter_Eta[1]-daughter_Eta[0])**2+dPhi**2)**.5 
	#dR2 = ((daughter_Eta[3]-daughter_Eta[2])**2+(daughter_Phi[3]-daughter_Phi[2])**2)**.5 
	SdR4.Fill(dR1,1)
	#SdR4.Fill(dR2,1)
llp5 = _file5.Get("lldjNtuple/EventTree")
SdR5 = TH1F("Scalar_dR5",'',30, 0, 5)
for entry in llp5:
	daughter_Eta=llp5.llpDaughterEta
	daughter_Phi=llp5.llpDaughterPhi
	dPhi = daughter_Phi[1]-daughter_Phi[0]
	if dPhi>3.14:	
		dPhi = 6.28-dPhi
	dR1 = ((daughter_Eta[1]-daughter_Eta[0])**2+dPhi**2)**.5 
	#dR2 = ((daughter_Eta[3]-daughter_Eta[2])**2+(daughter_Phi[3]-daughter_Phi[2])**2)**.5 
	SdR5.Fill(dR1,1)
	#SdR5.Fill(dR2,1)
#llp6 = _file6.Get("lldjNtuple/EventTree")
#SdR6 = TH1F("Scalar_dR6",'',30, 0, 5)
#for entry in llp6:
#	daughter_Eta=llp6.llpDaughterEta
#	daughter_Phi=llp6.llpDaughterPhi
#	dPhi = daughter_Phi[1]-daughter_Phi[0]
#	if dPhi>3.14:	
#		dPhi = 6.28-dPhi
#	dR1 = ((daughter_Eta[1]-daughter_Eta[0])**2+dPhi**2)**.5 
#	#dR2 = ((daughter_Eta[3]-daughter_Eta[2])**2+(daughter_Phi[3]-daughter_Phi[2])**2)**.5 
#	SdR6.Fill(dR1,1)
#	#SdR5.Fill(dR2,1)
SdR0.SetMarkerSize(8)
SdR0.GetXaxis().SetTitle("#Delta R")
SdR0.GetYaxis().SetTitle("Events")
SdR0.GetYaxis().SetTitleOffset(1.5)
SdR0.Scale(1/SdR0.Integral())
SdR0.SetLineColor(1)
SdR0.Draw("HIST")
SdR0.GetYaxis().SetRangeUser(0,1)
SdR1.Scale(1/SdR1.Integral())
SdR1.SetLineColor(2)
SdR1.Draw("HIST SAME")
SdR2.Scale(1/SdR2.Integral())
SdR2.SetLineColor(3)
SdR2.Draw("HIST SAME")
SdR3.Scale(1/SdR3.Integral())
SdR3.SetLineColor(4)
SdR3.Draw("HIST SAME")
SdR4.Scale(1/SdR4.Integral())
SdR4.SetLineColor(5)
SdR4.Draw("HIST SAME")
SdR5.Scale(1/SdR5.Integral())
SdR5.SetLineColor(6)
SdR5.Draw("HIST SAME")
#SdR6.Scale(1/SdR6.Integral())
#SdR6.SetLineColor(12)
#SdR6.SetLineStyle(7)
#SdR6.Draw("HIST SAME")


legend = TLegend(0.55,0.65,0.85,0.85) 		
legend.SetTextSize(0.022)
legend.SetBorderSize(0)
legend.SetNColumns(2)
legend.SetFillColor(kWhite)
legend.AddEntry(SdR0,"#splitline{h125_llp20_}{ct100_Zdark}","l")
legend.AddEntry(SdR1,"#splitline{h150_llp20_}{ct100_Zdark}","l")
legend.AddEntry(SdR2,"#splitline{h175_llp20_}{ct100_Zdark}","l")
legend.AddEntry(SdR3,"#splitline{h200_llp20_}{ct100_Zdark}","l")
legend.AddEntry(SdR4,"#splitline{h250_llp20_}{ct100_Zdark}","l")
legend.AddEntry(SdR5,"#splitline{h500_llp20_}{ct100_Zdark}","l")
#legend.AddEntry(SdR6,"#splitline{ZH_MS55_}{ctau100}","l")
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
extra2.DrawLatexNDC(0.55,0.91,"Run2 ZH v. Zdark")
c1.Modified()
c1.Update()
c1.SaveAs("Zdark_llp20_dR100mm_v2.png")

k=raw_input('Press ENTER to exit')
