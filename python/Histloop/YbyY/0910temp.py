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


Region = ['loglead','logexclead']
TV = ['TTHad','QCDMu80120']
gROOT.ForceStyle(kTRUE)
	
for i in range(len(Region)):
	for j in range(len(TV)):
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
		Channel = Region[i]
		Var = TV[j]
		_file0 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/%s/ggH_HToSSTo4Tau_MH-125_MS-15_ctauS-100_tree.root' %Var,'read')
		_file2 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/%s/ST_s-channel_4f_hadronicDecays_tree.root' %Var,'read')
		_file3 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/%s/TTJets_tree.root' %Var,'read')
		_file4 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/%s/QCD_Pt-30to50_tree.root' %Var,'read')
		_file5 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/%s/QCD_Pt-50to80_tree.root' %Var,'read')

		h0=_file0.Get('%s' %Channel)
		h2=_file2.Get('%s' %Channel)
		h3=_file3.Get('%s' %Channel)
		h4=_file4.Get('%s' %Channel)
		h5=_file5.Get('%s' %Channel)

		h0.SetTitle('%s' %Channel)
		h0.GetXaxis().SetTitle('%s_%s' %(Var,Channel))
		h0.GetYaxis().SetTitle('Unit Normalized')
		h0.GetYaxis().SetTitleOffset(1.3)
		h0.Scale(1./h0.Integral())
		h0.SetLineColor(1)
		h0.Draw('HIST')
		h0.GetYaxis().SetRangeUser(0.00001,10)
	
		h2.Scale(1./h2.Integral())
		h2.SetLineColor(3)
		h2.Draw('HIST SAME')

		h3.Scale(1./h3.Integral())
		h3.SetLineColor(4)
		h3.Draw('HIST SAME')

		h4.Scale(1./h4.Integral())
		h4.SetLineColor(5)
		h4.Draw('HIST SAME')

		h5.Scale(1./h5.Integral())
		h5.SetLineColor(6)
		h5.Draw('HIST SAME')
	
		legend = TLegend(0.15,0.65,0.35,0.87) 		
   		legend.SetBorderSize(0)
		legend.SetTextSize(.0275)
    		#legend.SetNColumns(2)
   		legend.SetFillColor(kWhite)
   		legend.SetFillColor(kWhite)
		legend.AddEntry(h0,"ggH4T-15100","l")
		legend.AddEntry(h2,"ST-sHad","l")
		legend.AddEntry(h3,"TTJets","l")
		legend.AddEntry(h4,"QCDMu-3050","l")
		legend.AddEntry(h5,"QCDMu-5080","l")
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
		c1.SaveAs('Disc_%s_%s.pdf'%(Var,Channel))
k=raw_input('Press ENTER to exit')
