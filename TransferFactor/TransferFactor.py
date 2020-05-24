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


#Region = ['TwoEleDY','TwoMuDY']
Region = ['Ele','Mu']
TV = ['nSelectedAODCaloJetTag_varbin']
Unc = ['MES','EGS','LeptonSF','AMax','IPSig','TA','TagVars']
#Unc = ['MES','EGS']
gROOT.ForceStyle(kTRUE)
	
#gStyle.SetOptStat(0)
for j in range(len(TV)):
	for i in range(len(Region)):
		for k in range(len(Unc)):
			num = 1
			c1 = TCanvas( 'c%s' %num, 'Histogram Drawing Options', 200, 10, 700, 900 )
			c1.SetGrid()
			gPad.SetLeftMargin(0.13)
			gPad.SetBottomMargin(0.12)
			gPad.SetTickx()
			gPad.SetTicky()
			gStyle.SetOptStat(0)
			gStyle.SetLineWidth(2)
			gStyle.SetHistLineWidth(2)
			Channel = Region[i]
			Var = TV[j]
			unc = Unc[k]
			file_object=open("TransferFactor_%s.txt"%Channel,"a")
			_file0 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/plots/CompleteTest_Full/Two%sZH/GH/log/Two%sZH_%s_GH_log.root' %(Channel,Channel,Var),'read')
			_file1 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/plots/CompleteTest_Full/Two%sDY/GH/log/Two%sDY_%s_GH_log.root' %(Channel,Channel,Var),'read')
			_file2 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/plots/CompleteTest_Full/Two%sZH/GH/log/Two%sZH_%s_GH_log_%sUp.root' %(Channel,Channel,Var,unc),'read')
			_file3 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/plots/CompleteTest_Full/Two%sDY/GH/log/Two%sDY_%s_GH_log_%sUp.root' %(Channel,Channel,Var,unc),'read')
			_file4 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/plots/CompleteTest_Full/Two%sZH/GH/log/Two%sZH_%s_GH_log_%sDown.root' %(Channel,Channel,Var,unc),'read')
			_file5 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/plots/CompleteTest_Full/Two%sDY/GH/log/Two%sDY_%s_GH_log_%sDown.root' %(Channel,Channel,Var,unc),'read')
			#h0=_file0.Get('h_%s_%s'%(Channel,Var))
			#h1=_file1.Get('h_%s_%s'%(Channel,Var))
			h0=_file0.Get('DY')
			h1=_file1.Get('DY')
			h2=_file2.Get('DY')
			h3=_file3.Get('DY')
			h4=_file4.Get('DY')
			h5=_file5.Get('DY')
			
			h0.Divide(h1)
			h0.SetTitle('%s_%s_%s Transfer Factor (ZH/DY)' %(Channel,Var,unc))
			h0.GetXaxis().SetTitle('%s' %Var)
			h0.GetYaxis().SetTitle('Sig_MS55ct100 ZH/DY ratio')
			h0.GetYaxis().SetTitleOffset(1.3)
			h0.SetLineColor(1)
			h0.Draw('HIST')
			h0.GetXaxis().SetRangeUser(0,4)
			if Channel == 'Ele':
				 h0.GetYaxis().SetRangeUser(0,4)
			else:	
				 h0.GetYaxis().SetRangeUser(0,.7)
	 		h6 = TH1F()
			h6 = h2.Clone('DY')	
			h2.Divide(h3)
			h2.SetLineColor(kRed)
			h2.Draw('HIST same')
	
			h7 = TH1F()
			h7 = h4.Clone('DY')
			h4.Divide(h5)
			h4.SetLineColor(kBlue)
			h4.Draw('HIST same')
			h4.GetXaxis().SetRangeUser(0,4)
	
			#h1.SetLineColor(1)
			#h1.Draw('HIST SAME')
	
			h6.Divide(h5)
			h6.SetLineColor(kRed-5)
			h6.Draw('HIST same')
			h7.Divide(h3)
			h7.SetLineColor(kBlue-5)
			h7.Draw('HIST same')
			file_object.write(unc)
			file_object.write("     NoUnc      ratio      Up/Up     ratio     Down/Down      ratio      Up/Down      ratio      Down/Up      ratio   ")
			file_object.write("\n")
			
			for t in range(3):
				if t == 0 :
					file_object.write("1st bin ")
				if t == 1 :
					file_object.write("2nd bin ")
				if t == 2 :
					file_object.write("Inc bin ")
				f0 =round(h0.GetBinContent(t+1),7)
				f2 =round(h2.GetBinContent(t+1),7)
				f4 =round(h4.GetBinContent(t+1),7)
				f6 =round(h6.GetBinContent(t+1),7)
				f7 =round(h7.GetBinContent(t+1),7)
					 
				#file_object.write(str(round(h0.GetBinContent(i+1),7))+'   ' )
				#file_object.write(str(round(h2.GetBinContent(i+1),7))+'   ' )
				#file_object.write(str(round(h4.GetBinContent(i+1),7))+'   ' )
				#file_object.write(str(round(h6.GetBinContent(i+1),7))+'   ' )
				#file_object.write(str(round(h7.GetBinContent(i+1),7))+'   ' )
				file_object.write(str(f0)+'       ' )
				file_object.write(str(0.000000)+'       ' )
				file_object.write(str(f2)+'   ' )
				file_object.write(str(round((f2-f0)/f0,7))+'   ' )
				file_object.write(str(f4)+'   ' )
				file_object.write(str(round((f4-f0)/f0,7))+'   ' )
				file_object.write(str(f6)+'   ' )
				file_object.write(str(round((f6-f0)/f0,7))+'   ' )
				file_object.write(str(f7)+'   ' )
				file_object.write(str(round((f7-f0)/f0,7))+'   ' )
				file_object.write("\n")
			file_object.write("\n")
			
			legend = TLegend(0.15,0.65,0.35,0.75) 		
   			legend.SetBorderSize(0)
    			legend.SetNColumns(2)
   			legend.SetFillColor(kWhite)
			legend.AddEntry(h0,"No Unc","l")
			legend.AddEntry(h2,"Up/Up","l")
			legend.AddEntry(h4,"Down/Down","l")
			legend.AddEntry(h6,"Up/Down","l")
			legend.AddEntry(h7,"Down/Up","l")
			legend.Draw()
			#l = TLatex()
			#l.SetTextAlign(13)
			#l.SetTextSize(0.02)
			#l.DrawLatexNDC(0.23,0.92,"CMS #it{Preliminary}           2017 DataSet B,2018 DataSet C  (13TeV)")
			#l.DrawLatexNDC(0.23,0.62,"splitline{CMS #it{Preliminary}}{2016,2017,2018 full lumi}")
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
    			extra2.DrawLatexNDC(0.55,0.91,"Run2 16 DY TF")
			c1.Modified()
			c1.Update()
			k=raw_input('Press ENTER to exit')
			c1.SaveAs('trialDY_TF_%s_%s_%sUp.png'%(Channel,Var,unc))
file_object.close()
k=raw_input('Press ENTER to exit')
