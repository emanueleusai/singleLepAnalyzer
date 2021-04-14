import ROOT as r, math as m #needs 6.14 or greater
r.gROOT.SetBatch()

intcolor=[r.TColor.GetColor(i) for i in ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"]]
def compare(name,file_list,name_list,legend_list,normalize=False,drawoption='hE',xtitle='',ytitle='',minx=0,maxx=0,rebin=1,miny=0,maxy=0,textsizefactor=1,logy=False):
  c=r.TCanvas(name,'',600,600)
  c.SetLeftMargin(0.15)#
  c.SetRightMargin(0.05)#
  c.SetBottomMargin(0.11)
  c.SetTopMargin(0.25)
  legend=r.TLegend(0.0,0.76,0.99,1.04)
  legend.SetHeader('')
  legend.SetBorderSize(0)
  legend.SetTextFont(42)
  legend.SetLineColor(1)
  legend.SetLineStyle(1)
  legend.SetLineWidth(1)
  legend.SetFillColor(0)
  legend.SetFillStyle(0)
  histo_list=[]
  the_maxy=0
  for i in range(len(name_list)):
    # histo_list.append(file_list[i].Get(name_list[i]).Clone(name_list[i]+'_'+str(i)))
    histo_list.append(file_list[name_list[i]].Clone(name_list[i]+'_'+str(i)))
    if normalize:
      histo_list[-1].Scale(1.0/(histo_list[-1].Integral()+0.00000001))
    histo_list[-1].SetStats(0)
    histo_list[-1].SetLineWidth(3)
    histo_list[-1].SetLineColor(intcolor[i])
    histo_list[-1].SetTitle('')
    if rebin!=1:
      histo_list[-1].Rebin(rebin)
    the_maxy=max(the_maxy,histo_list[-1].GetBinContent(histo_list[-1].GetMaximumBin())*1.05)
    legend.AddEntry(histo_list[-1],legend_list[i],'l')
  a=r.TH1F('','',3,minx,maxx)
  a.Fill((1.0*maxx+minx)/2,the_maxy*1.2)
  a.SetMaximum(the_maxy)
  a.SetLineColor(0)
  a.SetStats(0)
  a.Draw('HIST')
  a.SetMaximum(the_maxy)
  for i in range(len(name_list)):
    if i==0:
      if miny!=0 or maxy!=0:
        histo_list[i].SetMaximum(maxy)
        histo_list[i].SetMinimum(miny)
      else:
        histo_list[i].SetMaximum(the_maxy)
        #histo_list[i].SetMinimum(0.0001)
      histo_list[i].Draw(drawoption+'SAME')
      charsize=0.05*textsizefactor
      histo_list[i].GetYaxis().SetLabelSize(charsize)
      histo_list[i].GetYaxis().SetTitleSize(charsize)
      histo_list[i].GetYaxis().SetTitleOffset(1.6)
      histo_list[i].GetXaxis().SetLabelSize(charsize)
      histo_list[i].GetXaxis().SetTitleSize(charsize)
      histo_list[i].GetXaxis().SetTitleOffset(0.95)
      if xtitle!='':
        histo_list[i].GetXaxis().SetTitle(xtitle)
      if ytitle!='':  
        histo_list[i].GetYaxis().SetTitle(ytitle)
      if maxx!=0 or minx!=0:
        histo_list[i].GetXaxis().SetRangeUser(minx,maxx)
    else:
      histo_list[i].Draw(drawoption+'SAME')
  if logy:
    c.SetLogy()
  legend.Draw()
  c.SaveAs('pdf/'+name+'.pdf')

years=['R17','R18']

# FWLJMET102X_1lep2017_Oct2019_4t_11072020_step3_40vars_4j/

postfixes=[
'40vars_4j',
'40vars_6j',
'50vars_4j',
'50vars_6j',
'73vars_4j',
'73vars_6j'
]

lumi={'R18':'59p97fb', 'R17':'41p53fb'}

cats=[
# 'E_nHOT0p_nT0p_nW0p_nB2p_nJ4',
# 'E_nHOT0p_nT0p_nW0p_nB2p_nJ4p',
# 'E_nHOT0p_nT0p_nW0p_nB2p_nJ5',
'E_nHOT0p_nT0p_nW0p_nB2p_nJ6p',
# 'M_nHOT0p_nT0p_nW0p_nB2p_nJ4',
# 'M_nHOT0p_nT0p_nW0p_nB2p_nJ4p',
# 'M_nHOT0p_nT0p_nW0p_nB2p_nJ5',
'M_nHOT0p_nT0p_nW0p_nB2p_nJ6p'
]

u='_'

proc=[
'tttt',
'ttnobb',
'ttbb',
'top',
'ewk',
'data_obs'
]

bkgs=[
'ttnobb',
'ttbb',
'top',
'ewk'
]

ttbars=[
'ttnobb',
'ttbb'
]

notts=[
'top',
'ewk'
]

outfile=r.TFile('comparison.root','recreate')
# outfile.cd()

plots={}
for y in years:
	for p in postfixes:
		# print 'templates_'+y+'_11072020k_'+p+'/templates_BDT_'+lumi[y]+'_rebinned_stat0p3.root'
		f=r.TFile('templates_'+y+'_11072020k_'+p+'/templates_BDT_'+lumi[y]+'_rebinned_stat0p3.root','r')
		for c in cats:
			ttbar=0
			bkg=0
			nott=0
			for q in proc:
			# BDT_59p97fb_isM_nHOT0p_nT0p_nW0p_nB2p_nJ4p__ewk;
				# print 'BDT_'+lumi[y]+'_is'+c+'__'+q
				plot=f.Get('BDT_'+lumi[y]+'_is'+c+'__'+q)
				if plot==None: continue 
				outfile.cd()
				plots[y+u+p+u+c+u+q]=plot.Clone()
				if q in bkgs:
					if bkg==0:
						bkg=plot.Clone()
					else:
						bkg.Add(plot)
				if q in ttbars:
					if ttbar==0:
						ttbar=plot.Clone()
					else:
						ttbar.Add(plot)
				if q in notts:
					if nott==0:
						nott=plot.Clone()
					else:
						nott.Add(plot)
			ttttcdf=plots[y+u+p+u+c+u+'tttt'].Clone()
			ttbarcdf=ttbar.Clone()
			ttttcdfnorm=ttttcdf.Integral()
			ttbarcdfnorm=ttbarcdf.Integral()
			imttmax=ttttcdf.GetNbinsX()+1
			for imtt in range(1,imttmax):
				ttttcdf.SetBinContent(imtt,plots[y+u+p+u+c+u+'tttt'].Integral(1,imtt)/ttttcdfnorm)
				ttbarcdf.SetBinContent(imtt,ttbar.Integral(1,imtt)/ttbarcdfnorm)

			plots[y+u+p+u+c+u+'ttbar'] = ttbar
			plots[y+u+p+u+c+u+'bkg'] = bkg
			plots[y+u+p+u+c+u+'nott'] = nott

			plots[y+u+p+u+c+u+'ttbarcdf'] = ttbarcdf
			plots[y+u+p+u+c+u+'ttttcdf'] = ttttcdf
			c1=r.TCanvas()
			ttbarcdf.Draw('hist')
			c1.SaveAs('pdf/'+y+u+p+u+c+u+'ttbarcdf.pdf')
			c2=r.TCanvas()
			ttttcdf.Draw('hist')
			c2.SaveAs('pdf/'+y+u+p+u+c+u+'ttttcdf.pdf')

		f.Close()

to_plot=[
'ttbar',
# 'bkg',
'tttt',
# 'data_obs',
'nott'
]

# print plots

for y in years:
	for c in cats:
		for q in to_plot:
			name_list=[]
			for p in postfixes:
				name_list.append(y+u+p+u+c+u+q)
			print name_list
			compare(name=y+u+c+u+q+'_comp_norebin' , textsizefactor=0.7 , normalize= False ,
		file_list=plots , legend_list=postfixes , name_list=name_list , drawoption= '',minx=-1,maxx=1)
			compare(name=y+u+c+u+q+'_comp' , textsizefactor=0.7 , normalize= False ,
		file_list=plots , legend_list=postfixes , name_list=name_list , drawoption= '', rebin=2,minx=-1,maxx=1 )
			compare(name=y+u+c+u+q+'_comp_smooth' , textsizefactor=0.7 , normalize= False ,
		file_list=plots , legend_list=postfixes , name_list=name_list , drawoption= 'HIST C', rebin=4,minx=-1,maxx=1 )
