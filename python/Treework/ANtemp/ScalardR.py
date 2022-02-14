from __future__ import division
from ROOT import *
import math
gROOT.ForceStyle(kTRUE)

c1 = TCanvas( 'c1', 'Histogram Drawing Options', 200, 10, 700, 900 )
gPad.SetGrid()
gPad.SetTickx()
gPad.SetTicky()
gStyle.SetOptStat(0)
gStyle.SetLineWidth(3)
gStyle.SetHistLineWidth(3)
gPad.SetLeftMargin(0.12)
gPad.SetBottomMargin(0.12)
_file0 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/suhoRutgersWH/ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/crab_ggH_HToSSTo4Tau_MH-125_2018/210704_070100/0000/ggH_HToSSTo4Tau_MH-125_16.list_MS-7_ctauS-100_.root','read')
_file1 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/suhoRutgersWH/ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/crab_ggH_HToSSTo4Tau_MH-125_2018/210704_150100/0000/ggH_HToSSTo4Tau_MH-125_16.list_MS-15_ctauS-100_.root','read')
_file2 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/suhoRutgersWH/ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/crab_ggH_HToSSTo4Tau_MH-125_2018/210704_400100/0000/ggH_HToSSTo4Tau_MH-125_16.list_MS-40_ctauS-100_.root','read')
_file3 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/suhoRutgersWH/ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/crab_ggH_HToSSTo4Tau_MH-125_2018/210704_550100/0000/ggH_HToSSTo4Tau_MH-125_16.list_MS-55_ctauS-100_.root','read')
SdR0 = TH1F("Scalar_dR0",'',80, 0, 8)
SdR1 = TH1F("Scalar_dR1",'',80, 0, 8)
SdR2 = TH1F("Scalar_dR2",'',80, 0, 8)
SdR3 = TH1F("Scalar_dR3",'',80, 0, 8)
llp0 = _file0.Get("TreeMakerMINIAOD/HiggsLongLived")
for entry in llp0:
	daughter=entry.PrunedGenParticles
	pdgInd = []
	i=0
	for flow in daughter:
		if abs(flow.pdgId()) == 9000006:
			pdgInd.append(i)
		i+=1
	if len(pdgInd) < 2:
		continue
	find = pdgInd[0]
	sind = pdgInd[1]
	dPhi = daughter[find].p4().phi()-daughter[sind].p4().phi()
	if dPhi > 3.14:	
		dPhi = 6.28-dPhi
	dR1 = ((daughter[find].p4().eta()-daughter[sind].p4().eta())**2+dPhi**2)**.5 
	SdR0.Fill(dR1,1)
llp1 = _file1.Get("TreeMakerMINIAOD/HiggsLongLived")
for entry in llp1:
	daughter=entry.PrunedGenParticles
	pdgInd = []
	i=0
	for flow in daughter:
		if abs(flow.pdgId()) == 9000006:
			pdgInd.append(i)
		i+=1
	if len(pdgInd) < 2:
		continue
	find = pdgInd[0]
	sind = pdgInd[1]
	dPhi = daughter[find].p4().phi()-daughter[sind].p4().phi()
	if dPhi > 3.14:	
		dPhi = 6.28-dPhi
	dR1 = ((daughter[find].p4().eta()-daughter[sind].p4().eta())**2+dPhi**2)**.5 
	SdR1.Fill(dR1,1)
llp2 = _file2.Get("TreeMakerMINIAOD/HiggsLongLived")
for entry in llp2:
	daughter=entry.PrunedGenParticles
	pdgInd = []
	i=0
	for flow in daughter:
		if abs(flow.pdgId()) == 9000006:
			pdgInd.append(i)
		i+=1
	if len(pdgInd) < 2:
		continue
	find = pdgInd[0]
	sind = pdgInd[1]
	dPhi = daughter[find].p4().phi()-daughter[sind].p4().phi()
	if dPhi > 3.14:	
		dPhi = 6.28-dPhi
	dR1 = ((daughter[find].p4().eta()-daughter[sind].p4().eta())**2+dPhi**2)**.5 
	SdR2.Fill(dR1,1)
llp3 = _file3.Get("TreeMakerMINIAOD/HiggsLongLived")
for entry in llp3:
	daughter=entry.PrunedGenParticles
	pdgInd = []
	i=0
	for flow in daughter:
		if abs(flow.pdgId()) == 9000006:
			pdgInd.append(i)
		i+=1
	if len(pdgInd) < 2:
		continue
	find = pdgInd[0]
	sind = pdgInd[1]
	dPhi = daughter[find].p4().phi()-daughter[sind].p4().phi()
	if dPhi > 3.14:	
		dPhi = 6.28-dPhi
	dR1 = ((daughter[find].p4().eta()-daughter[sind].p4().eta())**2+dPhi**2)**.5 
	SdR3.Fill(dR1,1)
#SpT.Sumw2()
SdR0.SetMarkerSize(8)
SdR0.SetTitle("")
SdR0.GetXaxis().SetTitle("#Delta R(S,S)")
SdR0.GetYaxis().SetTitle("Events")
SdR0.GetYaxis().SetTitleOffset(1.5)
SdR0.Scale(1/SdR0.Integral())
SdR0.SetLineColor(1)
SdR0.GetYaxis().SetRangeUser(0,0.1)
SdR0.Draw("HIST")
SdR1.Scale(1/SdR1.Integral())
SdR1.SetLineColor(2)
SdR1.Draw("HIST SAME")
SdR2.Scale(1/SdR2.Integral())
SdR2.SetLineColor(3)
SdR2.Draw("HIST SAME")
SdR3.Scale(1/SdR3.Integral())
SdR3.SetLineColor(4)
SdR3.Draw("HIST SAME")

legend = TLegend(0.5,0.55,0.8,0.75) 		
legend.SetBorderSize(0)
legend.AddEntry(SdR0,"m_{s} = 7GeV, c#tau=100mm","l")
legend.AddEntry(SdR1,"m_{s} = 15GeV, c#tau=100mm","l")
legend.AddEntry(SdR2,"m_{s} = 40GeV, c#tau=100mm","l")
legend.AddEntry(SdR3,"m_{s} = 55GeV, c#tau=100mm","l")
legend.SetTextSize(0.025);
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
title.DrawTextNDC(0.2,0.91,"CMS")
extra.DrawTextNDC(0.3,0.91,"Preliminary")
extra2.DrawLatexNDC(0.55,0.91,"Run2 13TeV")
extra = TLatex(1,1,"") 
extra.SetTextSize(0.03)
extra.SetTextColor(kBlack)
extra.SetTextFont(42)
extra.DrawLatexNDC(0.48,0.78,"pp #rightarrow ggH #rightarrow GluGluH(ss); s #rightarrow #tau#bar{#tau}")
c1.Modified()
c1.Update()
c1.SaveAs("Scalar_dR100mm.pdf")
k=raw_input('Press ENTER to exit')
