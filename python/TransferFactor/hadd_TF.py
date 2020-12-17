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
Samples = ['DY']
#Samples = ['ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-1','ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-10','ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-100','ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-1000','ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1','ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-10','ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-100','ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1000','ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-1','ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-10','ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-100','ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-1000']
Region = ['hadd']
TV = ['nSelectedAODCaloJetTag']
#Unc = ['MES','EGS','LeptonSF','AMax','IPSig','TA','TagVars']
Unc = ['JES']
gROOT.ForceStyle(kTRUE)
	
#gStyle.SetOptStat(0)
for m in range(len(Samples)):
#for m in range(3):
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
				sample = Samples[m]				
				Channel = Region[i]
				Var = TV[j]
				unc = Unc[k]
				file_object=open("TF_%s_%s_%s_%s.txt" %(Channel,Var,unc,sample),"a")
				_file3 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/plots/Limitsetup_JECSys/%sDY/%sDY_%s_GH_%sUp_wSF.root' %(Channel,Channel,Var,unc),'read')
				_file2 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/plots/Limitsetup_JECSys/%sZH/%sZH_%s_GH_%sUp_wSF.root' %(Channel,Channel,Var,unc),'read')
				_file5 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/plots/Limitsetup_JECSys/%sDY/%sDY_%s_GH_%sDown_wSF.root' %(Channel,Channel,Var,unc),'read')
				_file4 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/plots/Limitsetup_JECSys/%sZH/%sZH_%s_GH_%sDown_wSF.root' %(Channel,Channel,Var,unc),'read')
				_file1 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/plots/Limitsetup_JECSys/%sDY/%sDY_%s_GH_wSF.root' %(Channel,Channel,Var),'read')
				_file0 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/plots/Limitsetup_JECSys/%sZH/%sZH_%s_GH_wSF.root' %(Channel,Channel,Var),'read')
				h0=_file0.Get('DY')
				h1=_file1.Get('DY')
				h2=_file2.Get('DY')
				h3=_file3.Get('DY')
				h4=_file4.Get('DY')
				h5=_file5.Get('DY')

				h0.Divide(h1)
				h0.SetTitle('%s_%s_%s Transfer Factor (ZH/DY)' %(Channel,Var,unc))
				h0.GetXaxis().SetTitle('%s' %Var)
				h0.GetYaxis().SetTitle('%s ZH/DY ratio' %sample)
				h0.GetYaxis().SetTitleOffset(1.45)
				h0.GetYaxis().SetTitleSize(0.03)
				h0.SetLineColor(1)
				h0.Draw('HIST')
				print(h0.GetBinContent(3))			
				h0.GetXaxis().SetRangeUser(0,2)


		 		h6 = TH1F()
				h6 = h2.Clone()	
				print(h2.GetBinContent(3))			
				print(h6.GetBinContent(3))			
				h2.Divide(h3)
				h2.SetLineColor(kRed)
				h2.SetLineStyle(9)
				h2.Draw('HIST same')
				h2.GetXaxis().SetRangeUser(0,2)
		
				h7 = TH1F()
				h7 = h4.Clone()
				h4.Divide(h5)
				h4.SetLineColor(kBlue)
				h4.SetLineStyle(9)
				h4.Draw('HIST same')
				h4.GetXaxis().SetRangeUser(0,2)

				h6.Divide(h5)
				h6.SetLineColor(kMagenta)
				h6.SetLineStyle(2)
				h6.Draw('HIST same')
				h6.GetXaxis().SetRangeUser(0,2)
				print(h2.GetBinContent(3))			
				print(h6.GetBinContent(3))			

				h7.Divide(h3)
				h7.SetLineStyle(2)
				h7.SetLineColor(kGreen)
				h7.Draw('HIST same')
				h7.GetXaxis().SetRangeUser(0,2)


				highlist = [h0.GetMaximum(),h4.GetMaximum(),h7.GetMaximum()]
				lowlist = [h0.GetMinimum(),h4.GetMinimum(),h7.GetMinimum()]
				lowedge = min(lowlist)-0.2
				highedge = max(highlist)+0.2

				h0.GetYaxis().SetRangeUser(lowedge,highedge)


				file_object.seek(0)
				file_object.write(sample)
				file_object.write("\n")
				#file_object.write("      NoUnc            Up/Up      %diff       Down/Down       %diff       Up/Down       %diff       Down/Up       %diff   ")
				
				for t in range(3):
					if t == 0 :
						file_object.write("0Tag bin ")
						file_object.write("\n")
						file_object.write("      NoUnc          ")
						file_object.write("\n")
					if t == 1 :
						file_object.write("1Tag bin ")
						file_object.write("\n")
						file_object.write("      NoUnc          ")
						file_object.write("\n")
					if t == 2 :
						file_object.write("2Tag bin ")
						file_object.write("\n")
						file_object.write("      NoUnc          ")
						file_object.write("\n")
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
					file_object.write("\n")
					if f0 > 0 :
						file_object.write("      Up/Up    %diff      ")
						file_object.write("\n")
						file_object.write(str(f2)+'   ' )
						file_object.write(str(round((f2-f0)/f0,7))+'   ' )
						file_object.write("\n")
						file_object.write("      Down/Down    %diff      ")
						file_object.write("\n")
						file_object.write(str(f4)+'   ' )
						file_object.write(str(round((f4-f0)/f0,7))+'   ' )
						file_object.write("\n")
						file_object.write("      Up/Down    %diff      ")
						file_object.write("\n")
						file_object.write(str(f6)+'   ' )
						file_object.write(str(round((f6-f0)/f0,7))+'   ' )
						file_object.write("\n")
						file_object.write("      Down/Up    %diff      ")
						file_object.write("\n")
						file_object.write(str(f7)+'   ' )
						file_object.write(str(round((f7-f0)/f0,7))+'   ' )
						file_object.write("\n")
				file_object.write("\n")
	
				print(h0.GetBinContent(3))			
				print(h2.GetBinContent(3))			
				print(h4.GetBinContent(3))			
				print(h6.GetBinContent(3))			
				print(h7.GetBinContent(3))			


				file_object.truncate()
				legend = TLegend(0.40,0.75,0.63,0.85) 		
	   			legend.SetBorderSize(0)
	    			legend.SetNColumns(2)
	   			legend.SetFillColor(kWhite)
				legend.SetTextSize(0.020)
				legend.AddEntry(h0,"No Unc","l")
				legend.AddEntry(h2,"Up/Up","l")
				legend.AddEntry(h4,"Down/Down","l")
				legend.AddEntry(h6,"Up/Down","l")
				legend.AddEntry(h7,"Down/Up","l")
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
	    			extra2.DrawLatexNDC(0.55,0.91,"Run2 ErasGH 16.1/fb")
				c1.Modified()
				c1.Update()
				k=raw_input('Press ENTER to exit')
				c1.SaveAs('TF_%s_%s_%s_%s.png'%(Channel,Var,unc,sample))
file_object.close()                           
k=raw_input('Press ENTER to exit')            
