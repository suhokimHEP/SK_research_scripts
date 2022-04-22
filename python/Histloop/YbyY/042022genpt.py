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
from ROOT import *


gROOT.ForceStyle(kTRUE)
c1 = TCanvas( 'c1', 'Histogram Drawing Options', 0, 10, 700, 600 )
c1.SetGrid()
gPad.SetLeftMargin(0.13)
gPad.SetBottomMargin(0.12)
gPad.SetTickx()
gPad.SetTicky()
gPad.SetLogy()
gStyle.SetOptStat(0)
gStyle.SetLineWidth(3)
gStyle.SetHistLineWidth(3)
_file0 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/50ULATvar/Gen/QCD_Pt-15to20_tree.root','read')
_file1 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/50ULATvar/Gen/QCD_Pt-20to30_tree.root','read')
_file2 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/50ULATvar/Gen/QCD_Pt-30to50_tree.root','read')
_file3 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/50ULATvar/Gen/QCD_Pt-50to80_tree.root','read')
_file4 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/50ULATvar/Gen/QCD_Pt-80to120_tree.root','read')
_file5 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/50ULATvar/Gen/QCD_Pt-120to170_tree.root','read')
_file6 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/50ULATvar/Gen/QCD_Pt-170to300_tree.root','read')
_file7 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/50ULATvar/Gen/QCD_Pt-300to470_tree.root','read')
_file8 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/50ULATvar/Gen/QCD_Pt-470to600_tree.root','read')
_file9 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/50ULATvar/Gen/QCD_Pt-600to800_tree.root','read')

h0=_file0.Get('Stat23pT')
h1=_file1.Get('Stat23pT')
h2=_file2.Get('Stat23pT')
h3=_file3.Get('Stat23pT')
h4=_file4.Get('Stat23pT')
h5=_file5.Get('Stat23pT')
h6=_file6.Get('Stat23pT')
h7=_file7.Get('Stat23pT')
h8=_file8.Get('Stat23pT')
h9=_file9.Get('Stat23pT')
h0.GetXaxis().SetTitle('dijet genpT')
h0.GetYaxis().SetTitle('Event Number')
h0.GetYaxis().SetTitleOffset(1.3)
h0.SetLineColor(12)
h0.Scale(2799000)
h0.Draw('HIST')
h0.GetXaxis().SetRangeUser(0,1000)
h1.Scale(2526000)
h0.GetYaxis().SetRangeUser(0.01,10.*h1.GetMaximum())
h1.SetLineColor(1)
h1.Draw('HIST SAME')
h2.Scale(1362000)
h2.SetLineColor(2)
h2.Draw('HIST SAME')
h3.Scale(376600)
h3.SetLineColor(3)
h3.Draw('HIST SAME')
h4.Scale(88930)
h4.SetLineColor(4)
h4.Draw('HIST SAME')
h5.Scale(21230)
h5.SetLineColor(5)
h5.Draw('HIST SAME')
h6.Scale(7055)
h6.SetLineColor(6)
h6.Draw('HIST SAME')
h7.Scale(619.3)
h7.SetLineColor(7)
h7.Draw('HIST SAME')
h8.Scale(59.24)
h8.SetLineColor(8)
h8.Draw('HIST SAME')
h9.Scale(25.09)
h9.SetLineColor(9)
h9.Draw('HIST SAME')

bgstack = THStack("bgstack","")
bgstack.Add(h0)
bgstack.Add(h1)
bgstack.Add(h2)
bgstack.Add(h3)
bgstack.Add(h4)
bgstack.Add(h5)
bgstack.Add(h6)
bgstack.Add(h7)
bgstack.Add(h8)
bgstack.Add(h9)


legend = TLegend(0.55,0.45,0.75,0.87) 		
legend.SetBorderSize(0)
legend.SetTextSize(.0375)
#legend.SetNColumns(2)
legend.SetFillColor(kWhite)
legend.SetFillColor(kWhite)
legend.AddEntry(h0,"QCD15to20","f")
legend.AddEntry(h1,"QCD20to30","f")
legend.AddEntry(h2,"QCD30to50","f")
legend.AddEntry(h3,"QCD50to80","f")
legend.AddEntry(h4,"QCD80to120","f")
legend.AddEntry(h5,"QCD120to170","f")
legend.AddEntry(h6,"QCD170to300","f")
legend.AddEntry(h7,"QCD300to470","f")
legend.AddEntry(h8,"QCD470to600","f")
legend.AddEntry(h9,"QCD600to800","f")
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
extra2.DrawLatexNDC(0.55,0.91,"Run2")
c1.Modified()
c1.Update()
#k=raw_input('Press ENTER to exit')
c1.SaveAs('Disc.pdf')
k=raw_input('Press ENTER to exit')