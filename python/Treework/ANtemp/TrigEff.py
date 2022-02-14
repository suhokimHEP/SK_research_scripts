from __future__ import division
from ROOT import *
import math
gROOT.ForceStyle(kTRUE)
TV="HLT_Mu7_IP4_part"
c1 = TCanvas( 'c1', 'Histogram Drawing Options', 200, 10, 700, 900 )
gPad.SetGrid()
gPad.SetTickx()
gPad.SetTicky()
gStyle.SetOptStat(0)
gStyle.SetLineWidth(3)
gStyle.SetHistLineWidth(3)
gPad.SetLeftMargin(0.12)
gPad.SetBottomMargin(0.12)
_MS15ct1 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/suhoRutgersWH/ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/crab_ggH_HToSSTo4Tau_MH-125_2018/210704_150001/0000/ggH_HToSSTo4Tau_MH-125_16.list_MS-15_ctauS-1_.root','read')
_MS40ct1 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/suhoRutgersWH/ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/crab_ggH_HToSSTo4Tau_MH-125_2018/210704_400001/0000/ggH_HToSSTo4Tau_MH-125_16.list_MS-40_ctauS-1_.root','read')
_MS55ct1 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/suhoRutgersWH/ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/crab_ggH_HToSSTo4Tau_MH-125_2018/210704_550001/0000/ggH_HToSSTo4Tau_MH-125_16.list_MS-55_ctauS-1_.root','read')

_MS7ct10 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/suhoRutgersWH/ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/crab_ggH_HToSSTo4Tau_MH-125_2018/210704_070010/0000/ggH_HToSSTo4Tau_MH-125_16.list_MS-7_ctauS-10_.root','read')
_MS15ct10 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/suhoRutgersWH/ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/crab_ggH_HToSSTo4Tau_MH-125_2018/210704_150010/0000/ggH_HToSSTo4Tau_MH-125_16.list_MS-15_ctauS-10_.root','read')
_MS40ct10 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/suhoRutgersWH/ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/crab_ggH_HToSSTo4Tau_MH-125_2018/210704_400010/0000/ggH_HToSSTo4Tau_MH-125_16.list_MS-40_ctauS-10_.root','read')
_MS55ct10 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/suhoRutgersWH/ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/crab_ggH_HToSSTo4Tau_MH-125_2018/210704_550010/0000/ggH_HToSSTo4Tau_MH-125_16.list_MS-55_ctauS-10_.root','read')

_MS7ct100 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/suhoRutgersWH/ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/crab_ggH_HToSSTo4Tau_MH-125_2018/210704_070100/0000/ggH_HToSSTo4Tau_MH-125_16.list_MS-7_ctauS-100_.root','read')
_MS15ct100 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/suhoRutgersWH/ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/crab_ggH_HToSSTo4Tau_MH-125_2018/210704_150100/0000/ggH_HToSSTo4Tau_MH-125_16.list_MS-15_ctauS-100_.root','read')
_MS40ct100 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/suhoRutgersWH/ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/crab_ggH_HToSSTo4Tau_MH-125_2018/210704_400100/0000/ggH_HToSSTo4Tau_MH-125_16.list_MS-40_ctauS-100_.root','read')
_MS55ct100 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/suhoRutgersWH/ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/crab_ggH_HToSSTo4Tau_MH-125_2018/210704_550100/0000/ggH_HToSSTo4Tau_MH-125_16.list_MS-55_ctauS-100_.root','read')

_MS7ct1000 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/suhoRutgersWH/ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/crab_ggH_HToSSTo4Tau_MH-125_2018/210704_071000/0000/ggH_HToSSTo4Tau_MH-125_16.list_MS-7_ctauS-1000_.root','read')
_MS15ct1000 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/suhoRutgersWH/ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/crab_ggH_HToSSTo4Tau_MH-125_2018/210704_151000/0000/ggH_HToSSTo4Tau_MH-125_16.list_MS-15_ctauS-1000_.root','read')
_MS40ct1000 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/suhoRutgersWH/ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/crab_ggH_HToSSTo4Tau_MH-125_2018/210704_401000/0000/ggH_HToSSTo4Tau_MH-125_16.list_MS-40_ctauS-1000_.root','read')
_MS55ct1000 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/suhoRutgersWH/ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/crab_ggH_HToSSTo4Tau_MH-125_2018/210704_551000/0000/ggH_HToSSTo4Tau_MH-125_16.list_MS-55_ctauS-1000_.root','read')

TrigMS7  = TH1F("TrigMS7",'',6, 0, 6)
TrigMS15 = TH1F("TrigMS15",'',6, 0, 6)
TrigMS40 = TH1F("TrigMS40",'',6, 0, 6)
TrigMS55 = TH1F("TrigMS55",'',6, 0, 6)

llpMS15ct1 = _MS15ct1.Get("TreeMakerMINIAOD/HiggsLongLived")
llpMS15ct1.Draw("%s"%TV);
tempMS15ct1 = llpMS15ct1.GetHistogram() 
TrigMS15.Fill(1,tempMS15ct1.GetMean())
llpMS40ct1 = _MS40ct1.Get("TreeMakerMINIAOD/HiggsLongLived")
llpMS40ct1.Draw("%s"%TV);
tempMS40ct1 = llpMS40ct1.GetHistogram() 
TrigMS40.Fill(1,tempMS40ct1.GetMean())
llpMS55ct1 = _MS55ct1.Get("TreeMakerMINIAOD/HiggsLongLived")
llpMS55ct1.Draw("%s"%TV);
tempMS55ct1 = llpMS55ct1.GetHistogram() 
TrigMS55.Fill(1,tempMS55ct1.GetMean())

llpMS7ct10 = _MS7ct10.Get("TreeMakerMINIAOD/HiggsLongLived")
llpMS7ct10.Draw("%s"%TV);
tempMS7ct10 = llpMS7ct10.GetHistogram() 
TrigMS7.Fill(2,tempMS7ct10.GetMean())
llpMS15ct10 = _MS15ct10.Get("TreeMakerMINIAOD/HiggsLongLived")
llpMS15ct10.Draw("%s"%TV);
tempMS15ct10 = llpMS15ct10.GetHistogram() 
TrigMS15.Fill(2,tempMS15ct10.GetMean())
llpMS40ct10 = _MS40ct10.Get("TreeMakerMINIAOD/HiggsLongLived")
llpMS40ct10.Draw("%s"%TV);
tempMS40ct10 = llpMS40ct10.GetHistogram() 
TrigMS40.Fill(2,tempMS40ct10.GetMean())
llpMS55ct10 = _MS55ct10.Get("TreeMakerMINIAOD/HiggsLongLived")
llpMS55ct10.Draw("%s"%TV);
tempMS55ct10 = llpMS55ct10.GetHistogram() 
TrigMS55.Fill(2,tempMS55ct10.GetMean())

llpMS7ct100 = _MS7ct100.Get("TreeMakerMINIAOD/HiggsLongLived")
llpMS7ct100.Draw("%s"%TV);
tempMS7ct100 = llpMS7ct100.GetHistogram() 
TrigMS7.Fill(3,tempMS7ct100.GetMean())
llpMS15ct100 = _MS15ct100.Get("TreeMakerMINIAOD/HiggsLongLived")
llpMS15ct100.Draw("%s"%TV);
tempMS15ct100 = llpMS15ct100.GetHistogram() 
TrigMS15.Fill(3,tempMS15ct100.GetMean())
llpMS40ct100 = _MS40ct100.Get("TreeMakerMINIAOD/HiggsLongLived")
llpMS40ct100.Draw("%s"%TV);
tempMS40ct100 = llpMS40ct100.GetHistogram() 
TrigMS40.Fill(3,tempMS40ct100.GetMean())
llpMS55ct100 = _MS55ct100.Get("TreeMakerMINIAOD/HiggsLongLived")
llpMS55ct100.Draw("%s"%TV);
tempMS55ct100 = llpMS55ct100.GetHistogram() 
TrigMS55.Fill(3,tempMS55ct100.GetMean())

llpMS7ct1000 = _MS7ct1000.Get("TreeMakerMINIAOD/HiggsLongLived")
llpMS7ct1000.Draw("%s"%TV);
tempMS7ct1000 = llpMS7ct1000.GetHistogram() 
TrigMS7.Fill(4,tempMS7ct1000.GetMean())
llpMS15ct1000 = _MS15ct1000.Get("TreeMakerMINIAOD/HiggsLongLived")
llpMS15ct1000.Draw("%s"%TV);
tempMS15ct1000 = llpMS15ct1000.GetHistogram() 
TrigMS15.Fill(4,tempMS15ct1000.GetMean())
llpMS40ct1000 = _MS40ct1000.Get("TreeMakerMINIAOD/HiggsLongLived")
llpMS40ct1000.Draw("%s"%TV);
tempMS40ct1000 = llpMS40ct1000.GetHistogram() 
TrigMS40.Fill(4,tempMS40ct1000.GetMean())
llpMS55ct1000 = _MS55ct1000.Get("TreeMakerMINIAOD/HiggsLongLived")
llpMS55ct1000.Draw("%s"%TV);
tempMS55ct1000 = llpMS55ct1000.GetHistogram() 
TrigMS55.Fill(4,tempMS55ct1000.GetMean())

TrigMS15.Draw("histp0L")
TrigMS15.SetTitle("")
TrigMS15.GetXaxis().SetTitle("c#tau[mm]")
TrigMS15.GetYaxis().SetTitle("B-Parking Trigger Efficiency")
TrigMS15.GetYaxis().SetTitleOffset(1.5)
TrigMS15.SetLineColor(1)
TrigMS15.GetYaxis().SetRangeUser(0,0.25)
TrigMS7.Draw("histp0L same")
TrigMS7.SetLineColor(2)
TrigMS40.Draw("histp0L same")
TrigMS40.SetLineColor(3)
TrigMS55.Draw("histp0L same")
TrigMS55.SetLineColor(4)

legend = TLegend(0.5,0.55,0.8,0.75) 		
legend.SetBorderSize(0)
legend.AddEntry(TrigMS7,"m_{s} = 7GeV","l")
legend.AddEntry(TrigMS15,"m_{s} = 15GeV","l")
legend.AddEntry(TrigMS40,"m_{s} = 40GeV","l")
legend.AddEntry(TrigMS55,"m_{s} = 55GeV","l")
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
extra.DrawLatexNDC(0.38,0.78,"pp #rightarrow ggH #rightarrow GluGluH(ss); s #rightarrow #tau#bar{#tau}")
c1.Modified()
c1.Update()
c1.SaveAs("TrigEff.pdf")
k=raw_input('Press ENTER to exit')
