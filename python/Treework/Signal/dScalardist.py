from __future__ import division
from ROOT import *
import math
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
#_file0 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/Ntuple_Zdark/h175_llp20_ct1_evt100000/crab_h175_llp20_ct1/200415_221615/0000/lldjntuple_target.root','read')
#_file1 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/Ntuple_Zdark/h175_llp20_ct10_evt100000/crab_h175_llp20_ct10/200415_221702/0000/lldjntuple_target.root','read')
#_file2 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/Ntuple_Zdark/h175_llp20_ct100_evt100000/crab_h175_llp20_ct100/200415_221723/0000/lldjntuple_target.root','read')
#_file3 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/Ntuple_Zdark/h175_llp20_ct1000_evt100000/crab_h175_llp20_ct1000/200415_221744/0000/lldjntuple_target.root','read')
_file0 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/Ntuple_Zdark/h175_llp50_ct1_evt100000/crab_h175_llp50_ct1/200415_221805/0000/lldjntuple_target.root','read')
_file1 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/Ntuple_Zdark/h175_llp50_ct10_evt100000/crab_h175_llp50_ct10/200415_221825/0000/lldjntuple_target.root','read')
_file2 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/Ntuple_Zdark/h175_llp50_ct100_evt100000/crab_h175_llp50_ct100/200415_221842/0000/lldjntuple_target.root','read')
_file3 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/Ntuple_Zdark/h175_llp50_ct1000_evt100000/crab_h175_llp50_ct1000/200415_221859/0000/lldjntuple_target.root','read')
SpT0 = TH1F("Scalar_dist0",'',100, 0, 10000)
SpT1 = TH1F("Scalar_dist1",'',100, 0, 10000)
SpT2 = TH1F("Scalar_dist2",'',100, 0, 10000)
SpT3 = TH1F("Scalar_dist3",'',100, 0, 10000)
llp0 = _file0.Get("lldjNtuple/EventTree")
llp1 = _file1.Get("lldjNtuple/EventTree")
llp2 = _file2.Get("lldjNtuple/EventTree")
llp3 = _file3.Get("lldjNtuple/EventTree")
mother1, daughter1, diff1 = TVector3(),TVector3(),TVector3()
mother2, daughter2, diff2 = TVector3(),TVector3(),TVector3()
mother3, daughter3, diff3 = TVector3(),TVector3(),TVector3()
mother4, daughter4, diff4 = TVector3(),TVector3(),TVector3()
for entry in llp0:
	llpvX=llp0.llpvX
	llpvY=llp0.llpvY
	llpvZ=llp0.llpvZ
	llpDaughtervX=llp0.llpDaughtervX
	llpDaughtervY=llp0.llpDaughtervY
	llpDaughtervZ=llp0.llpDaughtervZ
	ps = llpvX.size()-1
	ds = llpDaughtervX.size()-1
	for Pt in llpvX:
                mother1.SetXYZ(llpvX.at(ps),llpvY.at(ps),llpvZ.at(ps));
                daughter1.SetXYZ(llpDaughtervX.at(ds),llpDaughtervY.at(ds),llpDaughtervZ.at(ds));
                diff1.SetXYZ(mother1.X()-daughter1.X(),mother1.Y()-daughter1.Y(),mother1.Z()-daughter1.Z());
		Final = diff1.Mag()
		SpT0.Fill(10*Final,1)
for entry in llp1:
	llpvX=llp1.llpvX
	llpvY=llp1.llpvY
	llpvZ=llp1.llpvZ
	llpDaughtervX=llp1.llpDaughtervX
	llpDaughtervY=llp1.llpDaughtervY
	llpDaughtervZ=llp1.llpDaughtervZ
	ps = llpvX.size()-1
	ds = llpDaughtervX.size()-1
	for Pt in llpvX:
                mother2.SetXYZ(llpvX.at(ps),llpvY.at(ps),llpvZ.at(ps));
                daughter2.SetXYZ(llpDaughtervX.at(ds),llpDaughtervY.at(ds),llpDaughtervZ.at(ds));
                diff2.SetXYZ(mother2.X()-daughter2.X(),mother2.Y()-daughter2.Y(),mother2.Z()-daughter2.Z());
		Final = diff2.Mag()
		SpT1.Fill(10*Final,1)
for entry in llp2:
	llpvX=llp2.llpvX
	llpvY=llp2.llpvY
	llpvZ=llp2.llpvZ
	llpDaughtervX=llp2.llpDaughtervX
	llpDaughtervY=llp2.llpDaughtervY
	llpDaughtervZ=llp2.llpDaughtervZ
	ps = llpvX.size()-1
	ds = llpDaughtervX.size()-1
	for Pt in llpvX:
                mother3.SetXYZ(llpvX.at(ps),llpvY.at(ps),llpvZ.at(ps));
                daughter3.SetXYZ(llpDaughtervX.at(ds),llpDaughtervY.at(ds),llpDaughtervZ.at(ds));
                diff3.SetXYZ(mother3.X()-daughter3.X(),mother3.Y()-daughter3.Y(),mother3.Z()-daughter3.Z());
		Final = diff3.Mag()
		SpT2.Fill(10*Final,1)
for entry in llp3:
	llpvX=llp3.llpvX
	llpvY=llp3.llpvY
	llpvZ=llp3.llpvZ
	llpDaughtervX=llp3.llpDaughtervX
	llpDaughtervY=llp3.llpDaughtervY
	llpDaughtervZ=llp3.llpDaughtervZ
	ps = llpvX.size()-1
	ds = llpDaughtervX.size()-1
	for Pt in llpvX:
	        mother4.SetXYZ(llpvX.at(ps),llpvY.at(ps),llpvZ.at(ps));
	        daughter4.SetXYZ(llpDaughtervX.at(ds),llpDaughtervY.at(ds),llpDaughtervZ.at(ds));
	        diff4.SetXYZ(mother4.X()-daughter4.X(),mother4.Y()-daughter4.Y(),mother4.Z()-daughter4.Z());
		Final = diff4.Mag()
		SpT3.Fill(10*Final,1)
#SpT.Sumw2()
SpT0.SetMarkerSize(8)
SpT0.GetXaxis().SetTitle("#gamma * Z_{d} flight distance [mm]")
SpT0.GetYaxis().SetTitle("Events")
SpT0.GetYaxis().SetTitleOffset(1.5)
SpT0.Scale(1/SpT0.Integral())
SpT0.SetLineColor(1)
SpT0.GetYaxis().SetRangeUser(0.001,1)
SpT0.Draw("HIST")
SpT1.Scale(1/SpT1.Integral())
SpT1.SetLineColor(2)
SpT1.Draw("HIST SAME")
SpT2.Scale(1/SpT2.Integral())
SpT2.SetLineColor(4)
SpT2.Draw("HIST SAME")
SpT3.Scale(1/SpT3.Integral())
SpT3.SetLineColor(5)
SpT3.Draw("HIST SAME")

legend = TLegend(0.3,0.55,0.6,0.75) 		
legend.SetBorderSize(0)
legend.AddEntry(SpT0,"#Phi_{m}=175GeV Z_{d}_{m} = 50GeV, c#tau=1mm","l")
legend.AddEntry(SpT1,"#Phi_{m}=175GeV Z_{d}_{m} = 50GeV, c#tau=10mm","l")
legend.AddEntry(SpT2,"#Phi_{m}=175GeV Z_{d}_{m} = 50GeV, c#tau=100mm","l")
legend.AddEntry(SpT3,"#Phi_{m}=175GeV Z_{d}_{m} = 50GeV, c#tau=1000mm","l")
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
extra.DrawLatexNDC(0.48,0.78,"pp #rightarrow #Phi #rightarrow Z (l^{+}l^{-})Z_{d}; Z_{d} #rightarrow b#bar{b}")
c1.Modified()
c1.Update()
c1.SaveAs("Zd_dist_llp50_2.pdf")
k=raw_input('Press ENTER to exit')
