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


Region = ['TwoEleOffZ']
TV = ['TransferFactor_m1toNo','TransferFactor_m1tomp3','TransferFactor_m1tomp5']
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
		gStyle.SetOptStat(0)
		gStyle.SetLineWidth(3)
		gStyle.SetHistLineWidth(3)
		Channel = Region[i]
		Var = TV[j]
		_file0 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/logCR/QCD_Pt-20to30_tree.root','read')
		_file1 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/logCR/ggH_HToSSTo4Tau_MH-125_MS-15_ctauS-100_tree.root','read')
		_file2 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/logCR/TTJets_tree.root','read')
		_file3 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/logCR/ST_t-channel_top_5f_tree.root','read')
		_file4 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/logCR/ST_s-channel_top_leptonDecays_tree.root','read')
		_file5 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/logCR/ST_s-channel_4f_hadronicDecays_tree.root','read')

		h0=_file0.Get('%s' %Var)
		h1=_file1.Get('%s' %Var)
		h2=_file2.Get('%s' %Var)
		h3=_file3.Get('%s' %Var)
		h4=_file4.Get('%s' %Var)
		h5=_file5.Get('%s' %Var)

		h0.SetTitle('%s' %Var)
		h0.GetXaxis().SetTitle('%s' %Var)
		h0.GetYaxis().SetTitle('Unit Normalized')
		h0.GetYaxis().SetTitleOffset(1.3)
		h0.Scale(1./h0.Integral())
		h0.SetLineColor(1)
		h0.Draw('HIST')
		h0.GetYaxis().SetRangeUser(0,0.25)

		h1.Scale(1./h1.Integral())
		h1.SetLineColor(2)
		h1.Draw('HIST SAME')
	
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


	
		legend = TLegend(0.75,0.75,0.85,0.87) 		
   		legend.SetBorderSize(0)
		legend.SetTextSize(.0175)
    		#legend.SetNColumns(2)
   		legend.SetFillColor(kWhite)
   		legend.SetFillColor(kWhite)
		legend.AddEntry(h0,"QCD-Mu","l")
		legend.AddEntry(h1,"ggH","l")
		legend.AddEntry(h2,"TTJets","l")
		legend.AddEntry(h3,"ST-t","l")
		legend.AddEntry(h4,"ST-sLept","l")
		legend.AddEntry(h5,"ST-sHad","l")
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
