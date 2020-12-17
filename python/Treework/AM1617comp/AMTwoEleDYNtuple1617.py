from __future__ import division
from ROOT import *
from math import *
import os
#-------------------------------------------------------------------------------
file2016 = []
file2017 = []
for file in os.listdir("/eos/uscms/store/group/lpchbb/LLDJntuples/topRWT/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_DY50_1/180928_181036/0000/"):
    if file.endswith(".root"):
        file2016.append(os.path.join("/eos/uscms/store/group/lpchbb/LLDJntuples/topRWT/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_DY50_1/180928_181036/0000/", file))
#print(file2016)
for file in os.listdir("/eos/uscms/store/group/lpchbb/LLDJntuples/2017_LLDJ/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DY50_1/190305_221053/0000/"):
    if file.endswith(".root"):
        file2017.append(os.path.join("/eos/uscms/store/group/lpchbb/LLDJntuples/2017_LLDJ/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DY50_1/190305_221053/0000/", file))
#print(file2017)
list2016 = []
list2017 = []
for i in range (2):
	list2016.append(file2016[i])
	list2017.append(file2017[i])
print(list2016)
print(list2017)

sample ='DYJetsToLL_M-50'   
# read all entries and fill the histograms
c1 = TCanvas('c1', 'Histogram', 200, 10, 700, 900)
hAm = TH1F("hTA",'%s Ntuple AOD_TA hist' % sample, 500, -5, 2)
hAmsize = TH1I("hAmsize","%s MC Ntuple AOD_TA size hist" % sample, 30, 0, 30)
hTrig = TH1I("hTrig",'%s Ntuple AOD_Ele23Ele12 hist' % sample, 300, 0, 300)
hSigAm = TH1F("hSigTA",'%s Ntuple AOD_TA hist in Ele23Ele12' % sample, 500, -5, 2)
counter = 0
acounter = 0	 
for root2016 in list2016:
    myfile = TFile.Open(root2016)
    mytree = myfile.Get("lldjNtuple/EventTree")
    entries = mytree.GetEntries()
    Jet = std.vector('float')(1)
    mytree.SetBranchAddress("AODCaloJetMedianLog10TrackAngle",Jet)
    #mytree.Print()     
    #print(entries)
    #DYPass = std.vector('Bool')(1) 
    #print(DYPass)
    #mytree.SetBranchAddress("AOD_HLT_Ele23Ele12",DYPass)	
    #print(DYPass)
    for entry in mytree:      
	counter = counter + int(Jet.size())
    	trig = entry.AOD_HLT_Ele23Ele12
    	AlphaMax = entry.AODCaloJetMedianLog10TrackAngle
    	#print(trig)
    	hTrig.Fill(trig,1)
    	#print(AlphaMax)
    	#hAmsize.Fill(number,1) 	
    	#decision = IDPass.at(i)
    	#print(decision)
    	for alpha in AlphaMax:
    		#print(alpha)
    		hAm.Fill(alpha,1)
    		if trig >0 :
    			acounter = acounter +1
			hSigAm.Fill(alpha,1)
    
print(counter)
print(acounter)
h7Am = TH1F("h7TA",'%s 2017 Ntuple AOD_TA hist' % sample, 500, -5, 2)
h7Amsize = TH1I("h7Amsize","%s 2017 MC Ntuple AOD_Am size hist" % sample, 30, 0, 30)
h7Trig = TH1I("h7Trig",'%s 2017 Ntuple AOD_Ele23Ele12 hist' % sample, 300, 0, 300)
h7SigAm = TH1F("h7SigTA",'%s 2017 Ntuple AOD_TA hist in Ele23Ele12' % sample, 500, -5, 2)
counter7 = 0
acounter7 = 0 
for root2017 in list2017:
    myfile7 = TFile.Open(root2017)
    mytree7 = myfile7.Get("lldjNtuple/EventTree")
    entries7 = mytree7.GetEntries()
    Jet7 = std.vector('float')(1)
    mytree.SetBranchAddress("AODCaloJetMedianLog10TrackAngle",Jet7)
    #mytree.Print()     
    #print(entries7)
    #DYPass = std.vector('Bool')(1) 
    #print(DYPass)
    #mytree.SetBranchAddress("AOD_HLT_Ele23Ele12",DYPass)	
    #print(DYPass)
    for entry in mytree7:      
    	counter7 = counter7 + int(Jet7.size())
    	trig = entry.AOD_HLT_Ele23Ele12
    	AlphaMax = entry.AODCaloJetMedianLog10TrackAngle
    	#print(trig)
    	h7Trig.Fill(trig,1)
    	#print(AlphaMax)
    	#hAmsize.Fill(number,1) 	
    	#decision = IDPass.at(i)
    	#print(decision)
    	for alpha in AlphaMax:
    		#print(alpha)
    		h7Am.Fill(alpha,1)
    		if trig >0 :
    			acounter7 = acounter7 +1
			h7SigAm.Fill(alpha,1)
print(counter7)
print(acounter7)
frac = float(counter/counter7) 
ratio = float(acounter/acounter7)
print(frac)
print(ratio)
h7Am.Scale(frac)
h7SigAm.Scale(ratio)
#hAmsize.Draw('HIST')
#c1.Modified()
#c1.Update()
#c1.SaveAs('%s_hAmsize.png' % sample)
#hAm.SetTitle('%s MC AOD_Am hist' % sample)
hAm.GetXaxis().SetTitle('AODCaloJetMedianLog10TrackAngle')
hAm.GetYaxis().SetTitle('Counts')
hAm.GetYaxis().SetRangeUser(0,1000)
hAm.SetFillStyle(3007)
hAm.SetFillColor(kBlue)
hAm.Draw('HIST')
h7Am.SetFillStyle(3006)
h7Am.SetFillColor(kRed)
h7Am.Draw('HIST SAME')
legend = TLegend(0.1,0.8,0.3,0.9)
legend.AddEntry(hAm,"2016 DYJetsToLL_M-50","f")
legend.AddEntry(h7Am,"2017 DYJetsToLL_M-50","f")
legend.Draw()
c1.Modified()
c1.Update()
c1.SaveAs('%s_h7TA.png' % sample)
hTrig.Draw('HIST')
c1.Modified()
c1.Update()
c1.SaveAs('%s_hTrig.png' % sample)
hSigAm.GetXaxis().SetTitle('AODCaloJetMedianLog10TrackAngle')
hSigAm.GetYaxis().SetTitle('Counts')
hSigAm.GetYaxis().SetRangeUser(0,200)
hSigAm.SetFillStyle(3007)
hSigAm.SetFillColor(kBlue)
hSigAm.Draw('HIST')
h7SigAm.SetFillStyle(3006)
h7SigAm.SetFillColor(kRed)
h7SigAm.Draw('HIST SAME')
legend2 = TLegend(0.1,0.8,0.3,0.9)
legend2.AddEntry(hSigAm,"2016 DYJetsToLL_M-50","f")
legend2.AddEntry(h7SigAm,"2017 DYJetsToLL_M-50","f")
legend2.Draw()
c1.Modified()
c1.Update()
c1.SaveAs('%s_h7SigTA.png' % sample)
h7Trig.Draw('HIST')
c1.Modified()
c1.Update()
c1.SaveAs('%s_h7Trig.png' % sample)

#legend = TLegend(0.7,0.65,0.9,0.75)
##legend.AddEntry(hEUp,"Electron pt EGSUp","lep")
##legend.AddEntry(hEDown,"Electron pt EGSDown","lep")
#legend.Draw()
#c1.Modified()
#c1.Update()
#c1.SaveAs('%s_hAm.png' % sample)

k=raw_input('Press ENTER to exit')

