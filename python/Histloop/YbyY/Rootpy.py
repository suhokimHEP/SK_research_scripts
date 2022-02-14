## \file
## A Simple histogram drawing example
##
## \macro_image
## \macro_output
## \macro_code

from __future__ import division
from ROOT import *


TV = ['NoPunzi']
gROOT.ForceStyle(kTRUE)
	
for j in range(len(TV)):
	num = j
	c1 = TCanvas( 'c%s' %num, 'Histogram Drawing Options', 0, 10, 700, 600 )
	c1.SetGrid()
	gPad.SetLeftMargin(0.13)
	gPad.SetBottomMargin(0.12)
	gPad.SetTickx()
	gPad.SetTicky()
	gPad.SetLogy()
	gStyle.SetOptStat(0)
	gStyle.SetLineWidth(3)
	gStyle.SetHistLineWidth(3)
	Var = TV[j]
	_file0 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/fabsIP_Oct7/2p250CutTools/ggH_HToSSTo4Tau_MH-125_MS-15_ctauS-100_tree.root','read')
	_file1 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/fabsIP_Oct7/2p250CutTools/QCD_Pt-50to80_tree.root','read')

	h0=_file0.Get('exclead')
	h1=_file1.Get('exclead')
	h0.GetXaxis().SetTitle('excleadROI score')
	h0.GetYaxis().SetTitle('Unit Normalized')
	h0.GetYaxis().SetTitleOffset(1.3)
	h0.Scale(1./h0.Integral())
	h0.SetLineColor(1)
	h0.Draw('HIST')
	h0.GetXaxis().SetRangeUser(0.3,1.0)
	h0.GetYaxis().SetRangeUser(0.001,1.0)

	h1.Scale(1./h1.Integral())
	h1.SetLineColor(2)
	h1.Draw('HIST SAME')
	
	legend = TLegend(0.55,0.75,0.75,0.87) 		
	legend.SetBorderSize(0)
	legend.SetTextSize(.0375)
	#legend.SetNColumns(2)
	legend.SetFillColor(kWhite)
	legend.SetFillColor(kWhite)
	legend.AddEntry(h0,"ggH-MS15-ct100","l")
	legend.AddEntry(h1,"QCD-50to80","l")
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
	c1.SaveAs('Disc_%s.pdf'%Var)
k=raw_input('Press ENTER to exit')
