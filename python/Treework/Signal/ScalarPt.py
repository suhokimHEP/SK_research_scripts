from __future__ import division
from ROOT import *
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
_file0 = TFile.Open('/uscms/home/skim2/nobackup/displacedZH_for_Suho/ZH_ms15_ctau100mm_s_to_bb/displacedJetMuon_ntupler.root','read')
_file1 = TFile.Open('/uscms/home/skim2/nobackup/displacedZH_for_Suho/ZH_ms40_ctau100mm_s_to_bb/displacedJetMuon_ntupler.root','read')
_file2 = TFile.Open('/uscms/home/skim2/nobackup/displacedZH_for_Suho/ZH_ms55_ctau100mm_s_to_bb/displacedJetMuon_ntupler.root','read')
SpT0 = TH1F("Scalar_pT0",'',40, 0, 200)
SpT1 = TH1F("Scalar_pT1",'',40, 0, 200)
SpT2 = TH1F("Scalar_pT2",'',40, 0, 200)
llp0 = _file0.Get("ntuples/llp")
llp1 = _file1.Get("ntuples/llp")
llp2 = _file2.Get("ntuples/llp")
for entry in llp0:
	Scalar_pT=llp0.gLLP_pt
	for Pt in Scalar_pT:
		SpT0.Fill(Pt,1)
for entry in llp1:
	Scalar_pT=llp1.gLLP_pt
	for Pt in Scalar_pT:
		SpT1.Fill(Pt,1)
for entry in llp2:
	Scalar_pT=llp2.gLLP_pt
	for Pt in Scalar_pT:
		SpT2.Fill(Pt,1)
#SpT.Sumw2()
SpT0.SetMarkerSize(8)
SpT0.GetXaxis().SetTitle("Scalar pT[GeV]")
SpT0.GetYaxis().SetTitle("Events")
SpT0.GetYaxis().SetTitleOffset(1.5)
SpT0.Scale(1/SpT0.Integral())
SpT0.SetLineColor(1)
SpT0.GetYaxis().SetRangeUser(0,0.1)
SpT0.Draw("HIST")
SpT1.Scale(1/SpT1.Integral())
SpT1.SetLineColor(2)
SpT1.Draw("HIST SAME")
SpT2.Scale(1/SpT2.Integral())
SpT2.SetLineColor(4)
SpT2.Draw("HIST SAME")

legend = TLegend(0.5,0.55,0.8,0.75) 		
legend.SetBorderSize(0)
legend.AddEntry(SpT0,"m_{s} = 15GeV, c#tau=100mm","l")
legend.AddEntry(SpT1,"m_{s} = 40GeV, c#tau=100mm","l")
legend.AddEntry(SpT2,"m_{s} = 55GeV, c#tau=100mm","l")
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
extra.DrawLatexNDC(0.48,0.78,"pp #rightarrow ZH #rightarrow Z (l^{+}l^{-})H(ss); s #rightarrow b#bar{b}")
c1.Modified()
c1.Update()
c1.SaveAs("Scalar_pT100mm.pdf")
k=raw_input('Press ENTER to exit')
