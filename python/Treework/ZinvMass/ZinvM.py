from ROOT import *
from math import *
#-------------------------------------------------------------------------------
rootfile ='/eos/uscms/store/group/lpchbb/LLDJntuples/topRWT/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_DY50_1/180928_181036/0000/lldjntuple_mc_AOD_1.root'
datafile = '/eos/uscms/store/group/lpchbb/LLDJntuples/topRWT/DoubleEG/crab_Data_DoubleEG_G/180928_191949/0000/lldjntuple_data_AOD_1.root'

   
# read all entries and fill the histograms
c1 = TCanvas('c1', 'Histogram', 200, 10, 700, 900)
hZ = TH1F("hZ","DY MC Ntuple Zmass hist", 50, 0, 200)
uhZ = TH1F("uhZ","DY MC Ntuple Zmass hist EGSUp", 50, 0, 200)
dhZ = TH1F("dhZ","DY MC Ntuple Zmass hist EGSDown", 50, 0, 200)
datahZ = TH1F("datahZ","DoubleEG Ntuple Zmass hist", 50, 0, 200)
gROOT.ForceStyle()
myfile = TFile.Open(rootfile)
mytree = myfile.Get("lldjNtuple/EventTree")
entries = mytree.GetEntries()
#mytree.Print()     
print(entries)
pt = mytree.GetLeaf("AOD_elePt")
print(pt)
ePt = std.vector('float')(1) 
print(ePt)
mytree.SetBranchAddress("AOD_elePt",ePt)	
print(ePt)
Eta = mytree.GetLeaf("AOD_eleEta")
print(Eta)
eEta = std.vector('float')(1)  
print(eEta)
mytree.SetBranchAddress("AOD_eleEta",eEta)        
print(eEta)
ePhi = std.vector('float')(1)  
print(ePhi)
mytree.SetBranchAddress("AOD_elePhi",ePhi)        
print(ePhi)
eChar = std.vector('int')(1)  
print(eChar)
mytree.SetBranchAddress("AOD_eleCharge",eChar)        
print(eChar)

for i in range(entries):      
	numpy = mytree.GetEntry(i)
	number =int(ePt.size())
	if number < 2:
		continue
	evec0,evec1,Zmass = TLorentzVector(), TLorentzVector(), TLorentzVector()
	#print(number)
	uevec0,uevec1,devec0,devec1 = TLorentzVector(), TLorentzVector(), TLorentzVector(), TLorentzVector()
	uZmass,dZmass = TLorentzVector(),TLorentzVector()
	for j in range(number):
		
		#print(ePt[j])
		#print(eEta[j])
		#print(eChar[j])
		if j == 0:
			energy = ePt[j]*cosh(eEta[j])
			Uenergy, Denergy = energy*1.02, energy*.98
			evec0.SetPtEtaPhiE(fabs(ePt[j]),eEta[j],ePhi[j],energy)				
			uevec0.SetPtEtaPhiE(fabs(ePt[j]),eEta[j],ePhi[j],Uenergy),devec0.SetPtEtaPhiE(fabs(ePt[j]),eEta[j],ePhi[j],Denergy)				
			#print(energy)
			#evec0.Print()
		if j == 1:	
			energy = ePt[j]*cosh(eEta[j])
			Uenergy, Denergy = energy*1.02, energy*.98
			#evec1.SetPtEtaPhiM(fabs(ePt[j]),eEta[j],ePhi[j],0.000511)
			evec1.SetPtEtaPhiE(fabs(ePt[j]),eEta[j],ePhi[j],energy)
			uevec1.SetPtEtaPhiE(fabs(ePt[j]),eEta[j],ePhi[j],Uenergy),devec1.SetPtEtaPhiE(fabs(ePt[j]),eEta[j],ePhi[j],Denergy)
			#print(energy)
	Zmass,uZmass,dZmass = evec0 + evec1,uevec0+uevec1,devec0+devec1
	
	#print(Zmass)			
	if eChar[0]*eChar[1] <0:
		hZ.Fill(Zmass.M(),1)			
		uhZ.Fill(uZmass.M(),1)			
		dhZ.Fill(dZmass.M(),1)			
		

myfile.Close()

yourfile = TFile.Open(datafile)
yourtree = yourfile.Get("lldjNtuple/EventTree")
yentries = yourtree.GetEntries()
#yourtree.Print()     
print(yentries)
ypt = yourtree.GetLeaf("AOD_elePt")
print(ypt)
yePt = std.vector('float')(1) 
print(yePt)
yourtree.SetBranchAddress("AOD_elePt",yePt)	
print(yePt)
yEta = yourtree.GetLeaf("AOD_eleEta")
print(yEta)
yeEta = std.vector('float')(1)  
print(yeEta)
yourtree.SetBranchAddress("AOD_eleEta",yeEta)        
print(yeEta)
yePhi = std.vector('float')(1)  
print(yePhi)
yourtree.SetBranchAddress("AOD_elePhi",yePhi)        
print(yePhi)
yeChar = std.vector('int')(1)  
print(yeChar)
yourtree.SetBranchAddress("AOD_eleCharge",yeChar)        
print(yeChar)
scale = float(entries)/float(yentries)
print(scale)
for i in range(yentries):      
	numpy = yourtree.GetEntry(i)
	number =int(yePt.size())
	if number < 2:
		continue
	evec0,evec1,Zmass = TLorentzVector(), TLorentzVector(), TLorentzVector()
	#print(number)
	for j in range(number):
		
		#print(ePt[j])
		#print(eEta[j])
		#print(eChar[j])
		if j == 0:
			yenergy = yePt[j]*cosh(yeEta[j])
			evec0.SetPtEtaPhiE(fabs(yePt[j]),yeEta[j],yePhi[j],yenergy)				
			#print(energy)
			#evec0.Print()
		if j == 1:	
			yenergy = yePt[j]*cosh(yeEta[j])
			#evec1.SetPtEtaPhiM(fabs(ePt[j]),eEta[j],ePhi[j],0.000511)
			evec1.SetPtEtaPhiE(fabs(yePt[j]),yeEta[j],yePhi[j],yenergy)
			#print(energy)
	Zmass = evec0 + evec1
	#print(Zmass)			
	if yeChar[0]*yeChar[1] <0:
		datahZ.Fill(Zmass.M(),1)			
#datahZ.Scale(scale)	
yourfile.Close()

hZ.SetTitle('DY MC Zmass')
hZ.GetXaxis().SetTitle('Zmass (GeV)')
hZ.GetYaxis().SetTitle('Counts')
hZ.GetYaxis().SetRangeUser(0,4000)
hZ.SetFillStyle(3003)
hZ.SetFillColor(kRed)
hZ.Draw('HIST')
uhZ.SetFillStyle(3006)
uhZ.SetFillColor(kYellow)
uhZ.Draw('HIST SAME')
dhZ.SetFillStyle(3007)
dhZ.SetFillColor(kBlue)
dhZ.Draw('HIST SAME')
datahZ.SetMarkerStyle(22)
datahZ.SetMarkerColor(2)
datahZ.Draw('p SAME')
legend8 = TLegend(0.7,0.65,0.9,0.75)
legend8.AddEntry(uhZ,"electron energy scale up","f")
legend8.AddEntry(dhZ,"electron energy scale down","f")
legend8.AddEntry(datahZ,"DoubleEG energy","lep")
legend8.Draw()
c1.Modified()
c1.Update()
c1.SaveAs('MC,Data_Zmass.png')


