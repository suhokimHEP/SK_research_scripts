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


Region = ['QCD_Pt-30to50','TTJets','ST_tW_top']
TV = ['log10(1-Excsublead)']
gROOT.ForceStyle(kTRUE)
	
for i in range(len(Region)):
	for j in range(len(TV)):
		num = i*j
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
		Channel = Region[i]
		Var = TV[j]
		_file0 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/logCR/%s_tree.root' %Channel,'read')

		h0=_file0.Get('Exclogsublead')
		h1=_file0.Get('mp5Exclogsublead')
		h2=_file0.Get('m1Exclogsublead')
		h0.GetXaxis().SetTitle('log10(1-Excsublead) score')
		h0.GetYaxis().SetTitle('Unit Normalized')
		h0.GetYaxis().SetTitleOffset(1.3)
		h0.GetXaxis().SetRangeUser(-3,0.0)
		h0.Scale(1./h0.Integral())
		h0.SetLineColor(1)
		h0.Draw('HIST')

		h1.Scale(1./h1.Integral())
		h1.SetLineColor(2)
		h1.Draw('HIST SAME')
		
		h2.Scale(1./h2.Integral())
		h2.SetLineColor(3)
		h2.Draw('HIST SAME')
		legend = TLegend(0.25,0.65,0.5,0.87) 		
   		legend.SetBorderSize(0)
		legend.SetTextSize(.0275)
    		#legend.SetNColumns(2)
   		legend.SetFillColor(kWhite)
   		legend.SetFillColor(kWhite)
		legend.AddEntry(h0,"No leadROIcut","l")
		legend.AddEntry(h1,"log(1-lead)<-0.5","l")
		legend.AddEntry(h2,"log(1-lead)<-1","l")
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
    		extra2.DrawLatexNDC(0.55,0.91,"2018 %s" %Channel)
		c1.Modified()
		c1.Update()
		#k=raw_input('Press ENTER to exit')
		c1.SaveAs('Disc_%s.png'%Channel)
k=raw_input('Press ENTER to exit')
