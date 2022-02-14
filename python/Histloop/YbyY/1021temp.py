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


TV = ['gendR']
gROOT.ForceStyle(kTRUE)
	
for j in range(len(TV)):
	c1 = TCanvas( 'c1', 'Histogram Drawing Options', 0, 10, 700, 600 )
	c1.SetGrid()
	gPad.SetLeftMargin(0.13)
	gPad.SetBottomMargin(0.12)
	gPad.SetTickx()
	gPad.SetTicky()
	gStyle.SetOptStat(0)
	gStyle.SetLineWidth(3)
	gStyle.SetHistLineWidth(3)
	Var = TV[j]
	_file0 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/ggH_HToSSTo4Tau_MH-125_MS-7_ctauS-100_here.root','read')
	_file1 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/ggH_HToSSTo4Tau_MH-125_MS-15_ctauS-100_here.root','read')
	_file2 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/ggH_HToSSTo4Tau_MH-125_MS-40_ctauS-100_here.root','read')
	_file3 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/ggH_HToSSTo4Tau_MH-125_MS-55_ctauS-100_here.root','read')

	T0=_file0.Get('ROITree')
	T1=_file1.Get('ROITree')
	T2=_file2.Get('ROITree')
	T3=_file3.Get('ROITree')
	T0.Draw('gendR>>h0(80,0,4)')
	h0 = T0.GetHistogram()
	T1.Draw('gendR>>h1(80,0,4)')
	h1 = T1.GetHistogram()
	T2.Draw('gendR>>h2(80,0,4)')
	h2 = T2.GetHistogram()
	T3.Draw('gendR>>h3(80,0,4)')
	h3 = T3.GetHistogram()
	h0.GetXaxis().SetTitle('#DeltaR(#tau,#tau)')
	h0.GetYaxis().SetTitle('Unit Normalized')
	h0.GetYaxis().SetTitleOffset(1.3)
	h0.Scale(1./h0.Integral())
	h0.SetLineColor(1)
	h0.Draw('HIST')

	h1.Scale(1./h1.Integral())
	h1.SetLineColor(2)
	h1.Draw('HIST SAME')
	
	h2.Scale(1./h2.Integral())
	h2.SetLineColor(3)
	h2.Draw('HIST SAME')
	h3.Scale(1./h3.Integral())
	h3.SetLineColor(4)
	h3.Draw('HIST SAME')
	line = TLine(0.4,0,0.4,h0.GetMaximum())
	line.SetLineColor(6)
	line.Draw()
	legend = TLegend(0.45,0.75,0.85,0.87) 		
	legend.SetBorderSize(0)
	legend.SetTextSize(.0275)
	#legend.SetNColumns(2)
	legend.SetFillColor(kWhite)
	legend.SetFillColor(kWhite)
	legend.AddEntry(h0,"Signal (MS,ctau)=(7GeV,100mm)","l")
	legend.AddEntry(h1,"15,100","l")
	legend.AddEntry(h2,"40,100","l")
	legend.AddEntry(h3,"55,100","l")
	legend.AddEntry(line,"Denotes #DeltaR=0.4","l")
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
	extra2.SetTextFont(62)
	title.DrawTextNDC(0.2,0.91,"CMS")
	extra.DrawTextNDC(0.3,0.91,"Preliminary")
	extra2.DrawLatexNDC(0.55,0.91,"Run2 2018")
	c1.Modified()
	c1.Update()
	#k=raw_input('Press ENTER to exit')
	c1.SaveAs('Disc_%s.pdf'%Var)
k=raw_input('Press ENTER to exit')
