from __future__ import division
from ROOT import *
gROOT.ForceStyle(kTRUE)

c1 = TCanvas( 'c1', 'Histogram Drawing Options', 200, 10, 700, 900 )
gPad.SetTickx()
gPad.SetTicky()
gPad.SetLogy()
gStyle.SetOptStat(0)
gStyle.SetLineWidth(3)
gStyle.SetHistLineWidth(3)
gPad.SetLeftMargin(0.12)
gPad.SetBottomMargin(0.12)
_file0 = TFile.Open('/uscms/home/skim2/nobackup/displacedZH_for_Suho/ZH_ms40_ctau1mm_s_to_bb/displacedJetMuon_ntupler.root','read')
_file1 = TFile.Open('/uscms/home/skim2/nobackup/displacedZH_for_Suho/ZH_ms40_ctau10mm_s_to_bb/displacedJetMuon_ntupler.root','read')
_file2 = TFile.Open('/uscms/home/skim2/nobackup/displacedZH_for_Suho/ZH_ms40_ctau100mm_s_to_bb/displacedJetMuon_ntupler.root','read')
_file3 = TFile.Open('/uscms/home/skim2/nobackup/displacedZH_for_Suho/ZH_ms40_ctau1000mm_s_to_bb/displacedJetMuon_ntupler.root','read')
llp0 = _file0.Get("ntuples/llp")
SdR0 = TH1F("Scalar_dR0",'',100, 0, 10000)
for entry in llp0:
	px=llp0.pvX
	py=llp0.pvY
	pz=llp0.pvZ
	decayx=llp0.gLLP_decay_vertex_x
	decayy=llp0.gLLP_decay_vertex_y
	decayz=llp0.gLLP_decay_vertex_z
	dR1 = ((px-decayx[0])**2+(py-decayy[0])**2+(pz-decayz[0])**2)**.5 
	dR2 = ((px-decayx[1])**2+(py-decayy[1])**2+(pz-decayz[1])**2)**.5 
	SdR0.Fill(10*dR1,1)
	SdR0.Fill(10*dR2,1)
llp1 = _file1.Get("ntuples/llp")
SdR1 = TH1F("Scalar_dR1",'',100, 0, 10000)
for entry in llp1:
	px=llp1.pvX
	py=llp1.pvY
	pz=llp1.pvZ
	decayx=llp1.gLLP_decay_vertex_x
	decayy=llp1.gLLP_decay_vertex_y
	decayz=llp1.gLLP_decay_vertex_z
	dR1 = ((px-decayx[0])**2+(py-decayy[0])**2+(pz-decayz[0])**2)**.5 
	dR2 = ((px-decayx[1])**2+(py-decayy[1])**2+(pz-decayz[1])**2)**.5 
	SdR1.Fill(10*dR1,1)
	SdR1.Fill(10*dR2,1)
llp2 = _file2.Get("ntuples/llp")
SdR2 = TH1F("Scalar_dR2",'',100, 0, 10000)
for entry in llp2:
	px=llp2.pvX
	py=llp2.pvY
	pz=llp2.pvZ
	decayx=llp2.gLLP_decay_vertex_x
	decayy=llp2.gLLP_decay_vertex_y
	decayz=llp2.gLLP_decay_vertex_z
	dR1 = ((px-decayx[0])**2+(py-decayy[0])**2+(pz-decayz[0])**2)**.5 
	dR2 = ((px-decayx[1])**2+(py-decayy[1])**2+(pz-decayz[1])**2)**.5 
	SdR2.Fill(10*dR1,1)
	SdR2.Fill(10*dR2,1)
llp3 = _file3.Get("ntuples/llp")
SdR3 = TH1F("Scalar_dR3",'',100, 0, 10000)
for entry in llp3:
	px=llp3.pvX
	py=llp3.pvY
	pz=llp3.pvZ
	decayx=llp3.gLLP_decay_vertex_x
	decayy=llp3.gLLP_decay_vertex_y
	decayz=llp3.gLLP_decay_vertex_z
	dR1 = ((px-decayx[0])**2+(py-decayy[0])**2+(pz-decayz[0])**2)**.5 
	dR2 = ((px-decayx[1])**2+(py-decayy[1])**2+(pz-decayz[1])**2)**.5 
	SdR3.Fill(10*dR1,1)
	SdR3.Fill(10*dR2,1)
SdR0.SetMarkerSize(8)
SdR0.GetXaxis().SetTitle("#gamma * scalar partivle flight distance [mm]")
SdR0.GetYaxis().SetTitle("Events")
SdR0.GetYaxis().SetTitleOffset(1.5)
SdR0.Scale(1/SdR0.Integral())
SdR0.GetYaxis().SetRangeUser(0.001,1)
SdR0.SetLineColor(1)
SdR0.Draw("HIST")
SdR1.Scale(1/SdR1.Integral())
SdR1.SetLineColor(2)
SdR1.Draw("HIST SAME")
SdR2.Scale(1/SdR2.Integral())
SdR2.SetLineColor(4)
SdR2.Draw("HIST SAME")
SdR3.Scale(1/SdR3.Integral())
SdR3.SetLineColor(5)
SdR3.Draw("HIST SAME")


legend = TLegend(0.55,0.55,0.8,0.75) 		
legend.SetBorderSize(0)
legend.AddEntry(SdR0,"m_{s} = 40GeV, c#tau=1mm","l")
legend.AddEntry(SdR1,"m_{s} = 40GeV, c#tau=10mm","l")
legend.AddEntry(SdR2,"m_{s} = 40GeV, c#tau=100mm","l")
legend.AddEntry(SdR3,"m_{s} = 40GeV, c#tau=1000mm","l")
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
c1.SaveAs("Scalar_MS40.pdf")

k=raw_input('Press ENTER to exit')
