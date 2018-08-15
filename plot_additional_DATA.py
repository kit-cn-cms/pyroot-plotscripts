from plot_cuts_DATA import *



if ABCDversion is 'ABCD1':
    generalselection=plotselection_ABCD1_general
    generalselection_0=plotselection_ABCD1_general_0
    generalselection_i=plotselection_ABCD1_general_i
    cut1=plotselection_W_tau21
    cut1_0=plotselection_W_tau21_0
    cut1_i=plotselection_W_tau21_i
    cut2=plotselection_B_CSV
    cut2_0=plotselection_B_CSV_0
    cut2_i=plotselection_B_CSV_i
    cut3=plotselection_tau32
    cut3_0=plotselection_tau32_0
    cut3_i=plotselection_tau32_i

    cut1_anti=plotselection_W_tau21_anti
    cut1_anti_0=plotselection_W_tau21_anti_0
    cut1_anti_i=plotselection_W_tau21_anti_i
    cut2_anti=plotselection_B_CSV_anti
    cut2_anti_0=plotselection_B_CSV_anti_0
    cut2_anti_i=plotselection_B_CSV_anti_i
    cut3_anti=plotselection_tau32_anti
    cut3_anti_0=plotselection_tau32_anti_0
    cut3_anti_i=plotselection_tau32_anti_i
    
    
    
    
if ABCDversion is 'ABCD2':
    generalselection=plotselection_ABCD2_general
    generalselection_0=plotselection_ABCD2_general_0
    generalselection_i=plotselection_ABCD2_general_i
    cut1=plotselection_W_tau21
    cut1_0=plotselection_W_tau21_0
    cut1_i=plotselection_W_tau21_i
    cut2=plotselection_B_CSV
    cut2_0=plotselection_B_CSV_0
    cut2_i=plotselection_B_CSV_i
    cut3=plotselection_t_MSD
    cut3_0=plotselection_t_MSD_0
    cut3_i=plotselection_t_MSD_i 

    cut1_anti=plotselection_W_tau21_anti
    cut1_anti_0=plotselection_W_tau21_anti_0
    cut1_anti_i=plotselection_W_tau21_anti_i
    cut2_anti=plotselection_B_CSV_anti
    cut2_anti_0=plotselection_B_CSV_anti_0
    cut2_anti_i=plotselection_B_CSV_anti_i
    cut3_anti=plotselection_t_MSD_anti
    cut3_anti_0=plotselection_t_MSD_anti_0
    cut3_anti_i=plotselection_t_MSD_anti_i 
    
    
if ABCDversion is 'ABCD3':
    generalselection=plotselection_ABCD3_general
    generalselection_0=plotselection_ABCD3_general_0
    generalselection_i=plotselection_ABCD3_general_i
    cut1=plotselection_W_tau21
    cut1_0=plotselection_W_tau21_0
    cut1_i=plotselection_W_tau21_i
    cut2=plotselection_B_CSV
    cut2_0=plotselection_B_CSV_0
    cut2_i=plotselection_B_CSV_i
    cut3=plotselection_W_MSD
    cut3_0=plotselection_W_MSD_0
    cut3_i=plotselection_W_MSD_i    

    cut1_anti=plotselection_W_tau21_anti
    cut1_anti_0=plotselection_W_tau21_anti_0
    cut1_anti_i=plotselection_W_tau21_anti_i
    cut2_anti=plotselection_B_CSV_anti
    cut2_anti_0=plotselection_B_CSV_anti_0
    cut2_anti_i=plotselection_B_CSV_anti_i
    cut3_anti=plotselection_W_MSD_anti
    cut3_anti_0=plotselection_W_MSD_anti_0
    cut3_anti_i=plotselection_W_MSD_anti_i
    
if ABCDversion is 'ABCD4':
    generalselection=plotselection_ABCD4_general
    generalselection_0=plotselection_ABCD4_general_0
    generalselection_i=plotselection_ABCD4_general_i
    cut1=plotselection_W_MSD
    cut1_0=plotselection_W_MSD_0
    cut1_i=plotselection_W_MSD_i
    cut2=plotselection_B_CSV
    cut2_0=plotselection_B_CSV_0
    cut2_i=plotselection_B_CSV_i
    cut3=plotselection_TprimeMass
    cut3_0=plotselection_TprimeMass_0
    cut3_i=plotselection_TprimeMass_i
    
    cut1_anti=plotselection_W_MSD_anti
    cut1_anti_0=plotselection_W_MSD_anti_0
    cut1_anti_i=plotselection_W_MSD_anti_i
    cut2_anti=plotselection_B_CSV_anti
    cut2_anti_0=plotselection_B_CSV_anti_0
    cut2_anti_i=plotselection_B_CSV_anti_i
    cut3_anti=plotselection_TprimeMass_anti
    cut3_anti_0=plotselection_TprimeMass_anti_0
    cut3_anti_i=plotselection_TprimeMass_anti_i
    
if ABCDversion is 'ABCD5':
    generalselection=plotselection_ABCD5_general
    generalselection_0=plotselection_ABCD5_general_0
    generalselection_i=plotselection_ABCD5_general_i
    
    
    
    cut1=plotselection_W_MSD
    cut1_0=plotselection_W_MSD_0
    cut1_i=plotselection_W_MSD_i
    cut2=plotselection_B_CSV
    cut2_0=plotselection_B_CSV_0
    cut2_i=plotselection_B_CSV_i
    cut3=plotselection_W_tau21
    cut3_0=plotselection_W_tau21_0
    cut3_i=plotselection_W_tau21_i
   
    cut1_anti=plotselection_W_MSD_anti
    cut1_anti_0=plotselection_W_MSD_anti_0
    cut1_anti_i=plotselection_W_MSD_anti_i
    cut2_anti=plotselection_B_CSV_anti
    cut2_anti_0=plotselection_B_CSV_anti_0
    cut2_anti_i=plotselection_B_CSV_anti_i
    cut3_anti=plotselection_W_tau21_anti
    cut3_anti_0=plotselection_W_tau21_anti_0
    cut3_anti_i=plotselection_W_tau21_anti_i
    
    
    
    if radi=='CHSSoftDrop':
        if WZwindow and fullWMSD:
            if old:
                Zprime_withtopbtag_systrate=0.026335429083
                Zprime_withtopbtag_systshape_m=-0.000014237
                Zprime_withtopbtag_systshape_c=1.01372
                Zprime_notopbtag_systrate=0.025035741394
                Zprime_notopbtag_systshape_m=-0.0000563142
                Zprime_notopbtag_systshape_c=1.10324
                            
            else:
                Zprime_withtopbtag_systrate=0.0437729147047
                Zprime_withtopbtag_systshape_m=-0.00000748147
                Zprime_withtopbtag_systshape_c=0.959254
                Zprime_notopbtag_systrate=0.0416820871399
                Zprime_notopbtag_systshape_m=-0.0000748556
                Zprime_notopbtag_systshape_c=1.111
            
    if radi=='CHSPruning':
        if (not WZwindow) and fullWMSD:
            if old:
                Zprime_withtopbtag_systrate=0.0615567929662
                Zprime_withtopbtag_systshape_m=0.00014254936429
                Zprime_withtopbtag_systshape_c=0.815448
                Zprime_notopbtag_systrate=0.0237731064005
                Zprime_notopbtag_systshape_m=-0.000079382
                Zprime_notopbtag_systshape_c=1.14017
            else:
                #Zprime_withtopbtag_systrate=0.0631991257386
                #Zprime_withtopbtag_systshape_m=0.00014254936429
                #Zprime_withtopbtag_systshape_c=1.12496
                #Zprime_notopbtag_systrate=0.049580483332 
                #Zprime_notopbtag_systshape_m=1.80738901046e-05
                #Zprime_notopbtag_systshape_c=1.09896
              if bottomWP=='medium':
                  if topWP=='loose':
                    #Zprime_withtopbtag_systrate=0.0736834218346
                    #Zprime_withtopbtag_systshape_m=0.000157325109262
                    #Zprime_withtopbtag_systshape_c=1.12496
                    #Zprime_notopbtag_systrate=0.0428972485948 
                    #Zprime_notopbtag_systshape_m=6.92106626942e-05
                    #Zprime_notopbtag_systshape_c=1.09896      
                    
                    Zprime_withtopbtag_systrate=0.100533388233
                    Zprime_withtopbtag_systshape_m=0.0001950250116
                    Zprime_withtopbtag_systshape_c=1.12496
                    Zprime_notopbtag_systrate=0.0485657524616 
                    Zprime_notopbtag_systshape_m=7.03893690402e-05
                    Zprime_notopbtag_systshape_c=1.09896                        
                  if topWP=='medium':
                    Zprime_withtopbtag_systrate=0.0556968382142
                    Zprime_withtopbtag_systshape_m=4.83210624517e-05
                    Zprime_withtopbtag_systshape_c=1.12496
                    Zprime_notopbtag_systrate=0.107405141995 
                    Zprime_notopbtag_systshape_m=0.000162216814803
                    Zprime_notopbtag_systshape_c=1.09896                       
              else:
                  if topWP=='loose':
                    Zprime_withtopbtag_systrate=0.0662402661262
                    Zprime_withtopbtag_systshape_m=4.92325674899e-05
                    Zprime_withtopbtag_systshape_c=1.12496
                    Zprime_notopbtag_systrate=0.0677149795161
                    Zprime_notopbtag_systshape_m=3.54398759094e-05
                    Zprime_notopbtag_systshape_c=1.09896                
                  if topWP=='medium':
                    Zprime_withtopbtag_systrate=0.0711833960603
                    Zprime_withtopbtag_systshape_m=2.10852089666e-06
                    Zprime_withtopbtag_systshape_c=1.12496
                    Zprime_notopbtag_systrate=0.0756599436301 
                    Zprime_notopbtag_systshape_m=1.89854920597e-05
                    Zprime_notopbtag_systshape_c=1.09896                     

                
if ABCDversion is 'ABCD6':
    generalselection=plotselection_ABCD6_general
    generalselection_0=plotselection_ABCD6_general_0
    generalselection_i=plotselection_ABCD6_general_i
    cut1=plotselection_B_CSV
    cut1_0=plotselection_B_CSV_0
    cut1_i=plotselection_B_CSV_i
    cut2=plotselection_W_tau21
    cut2_0=plotselection_W_tau21_0
    cut2_i=plotselection_W_tau21_i
    cut3=plotselection_t_MSD
    cut3_0=plotselection_t_MSD_0
    cut3_i=plotselection_t_MSD_i
  
    cut1_anti=plotselection_B_CSV_anti
    cut1_anti_0=plotselection_B_CSV_anti_0
    cut1_anti_i=plotselection_B_CSV_anti_i
    cut2_anti=plotselection_W_tau21_anti
    cut2_anti_0=plotselection_W_tau21_anti_0
    cut2_anti_i=plotselection_W_tau21_anti_i
    cut3_anti=plotselection_t_MSD_anti
    cut3_anti_0=plotselection_t_MSD_anti_0
    cut3_anti_i=plotselection_t_MSD_anti_i
    
if ABCDversion is 'ABCD7':
    generalselection=plotselection_ABCD7_general
    generalselection_0=plotselection_ABCD7_general_0
    generalselection_i=plotselection_ABCD7_general_i
    cut1=plotselection_B_CSV
    cut1_0=plotselection_B_CSV_0
    cut1_i=plotselection_B_CSV_i
    cut2=plotselection_t_MSD
    cut2_0=plotselection_t_MSD_0
    cut2_i=plotselection_t_MSD_i
    cut3=plotselection_W_MSD
    cut3_0=plotselection_W_MSD_0
    cut3_i=plotselection_W_MSD_i

    cut1_anti=plotselection_B_CSV_anti
    cut1_anti_0=plotselection_B_CSV_anti_0
    cut1_anti_i=plotselection_B_CSV_anti_i
    cut2_anti=plotselection_t_MSD_anti
    cut2_anti_0=plotselection_t_MSD_anti_0
    cut2_anti_i=plotselection_t_MSD_anti_i
    cut3_anti=plotselection_W_MSD_anti
    cut3_anti_0=plotselection_W_MSD_anti_0
    cut3_anti_i=plotselection_W_MSD_anti_i


#stringforPDFs="float Weight_pdf_variation_260001"
#stringforPDFs1="Weight_pdf_variation_260001"
#stringforPDFs2="""
#PDFweights.push_back(Weight_pdf_variation_260001);
#"""

pdf_normweightsttbar=[1.0285403928,0.990114159298,0.988584387133,1.01889332059,1.05237299927,0.990719379875,1.00301419012,0.989663113443,0.991213672507,1.01552978649,1.02919060016,0.993578383217,0.986258507017,0.989247880748,0.982315499527,0.990532531623,0.966543378558,0.984182264085,1.00121033535,0.98135925712,1.00565177648,1.0294786568,0.975096957768,1.02173090511,1.00232509869,1.01187842359,0.963790618158,0.993565976416,0.984103730765,0.994145810228,1.01694070493,1.019344479,1.01172956295,1.02709298741,0.962844423667,0.997843355474,0.980248409009,1.00381417816,1.01965674945,1.01152287811,1.00897608998,1.00672764538,1.02184748569,1.0104982065,1.01090950727,1.01372748795,0.997178341661,0.996356071703,0.991194332369,1.00457633422,1.00963244698,1.0099716397,1.00881927905,0.993733091322,1.00809331987,0.991929935383,0.990390359819,1.0093097003,0.986283737755,1.00761916317,1.00164630037,1.00108546959,1.00139198427,0.989844800211,0.990147536673,1.00950490752,0.960738336277,1.00176385194,1.0083175853,1.00345779683,1.01894242063,1.00451400139,1.01758593874,0.990464886279,1.00042586582,1.0414231102,1.02063812865,0.98302683342,1.00573007249,1.00645654393,1.00834027486,1.01479418482,0.978745112178,1.00152348867,0.999542226965,0.99713256733,0.987922642322,0.989194765429,0.976009425862,1.00978848378,1.00540542912,1.00768618879,0.988494121995,0.992451445508,0.982438151277,0.993567630021,0.996536555276,1.00522587406,0.979009767484,0.974661266971]

#stringforPDFs="float Weight_pdf_1"
#stringforPDFs1="Weight_pdf_1"
#stringforPDFs2="""
#PDFweights.push_back(Weight_pdf_1);
#"""
#stringforPDFs_new="float Weight_pdf_new_1"
#stringforPDFs1_new="Weight_pdf_new_1"
#stringforPDFs2_new="""
#PDFweights_new.push_back(Weight_pdf_new_1);
#"""

#stringforPDFs_refac="float Weight_pdf_refac_1"
#stringforPDFs1_refac="Weight_pdf_refac_1"
#stringforPDFs2_refac="""
#PDFweights_refac.push_back(Weight_pdf_refac_1);
#"""
#stringforPDFs3_refac="""
#float Weight_pdf_refac_1="""+str(pdf_normweightsttbar[0])+"""*(DoMCDataWeights_ttbaronly==1)+1.0*(DoMCDataWeights_ttbaronly==0);
#"""


#for i in range(2,100):
    ##if i<10:
        ##istring="00"+str(i)
    ##if i>9 and i<100:
        ##istring="0"+str(i)
    ##if i>99:
        ##istring=""+str(i)
    ##stringforPDFs=stringforPDFs+(", float Weight_nnpdf30_lo_as_0130_"+str(i))
    ##stringforPDFs1=stringforPDFs1+(", Weight_nnpdf30_lo_as_0130_"+str(i))
    ##stringforPDFs2=stringforPDFs2+("PDFweights.push_back(Weight_nnpdf30_lo_as_0130_"+str(i)+");")
    ##stringforPDFs=stringforPDFs+(", float Weight_pdf_variation_260"+istring)
    ##stringforPDFs1=stringforPDFs1+(", Weight_pdf_variation_260"+istring)
    ##stringforPDFs2=stringforPDFs2+("PDFweights.push_back(Weight_pdf_variation_260"+istring+");")
    #istring=str(i)
    #stringforPDFs=stringforPDFs+(", float Weight_pdf_"+istring)
    #stringforPDFs1=stringforPDFs1+(", Weight_pdf_"+istring)
    #stringforPDFs2=stringforPDFs2+("PDFweights.push_back(Weight_pdf_"+istring+");")
    #stringforPDFs_new=stringforPDFs_new+(", float Weight_pdf_new_"+istring)
    #stringforPDFs1_new=stringforPDFs1_new+(", Weight_pdf_new_"+istring)
    #stringforPDFs2_new=stringforPDFs2_new+("PDFweights_new.push_back(Weight_pdf_new_"+istring+");")    #print stringforPDFs

    #stringforPDFs_refac=stringforPDFs_refac+(", float Weight_pdf_refac_"+istring)
    #stringforPDFs1_refac=stringforPDFs1_refac+(", Weight_pdf_refac_"+istring)
    #stringforPDFs2_refac=stringforPDFs2_refac+("PDFweights_refac.push_back(Weight_pdf_refac_"+istring+");")    #print stringforPDFs
    #stringforPDFs3_refac=stringforPDFs3_refac+("float Weight_pdf_refac_"+istring+"="+str(pdf_normweightsttbar[i-1])+"*(DoMCDataWeights_ttbaronly==1)+1.0*(DoMCDataWeights_ttbaronly==0);")    #print stringforPDFs


additionalfunctions=[
                        #'float temp=1',
                        #for(int i; i<N_Sideband_top_withbtag_anti_Topfirst_Bottoms;i++){temp*=(Sideband_top_withbtag_anti_Topfirst_Bottoms_CSVv2[i]<0.46);};',
                        ##"float anti_loose_btag(const float* bottomCSVs, int sizeofarray){"+"\n"+"   float anti_tag=1;"+"\n"+"      for (int i=0;  i<sizeofarray;i++){"+"\n"+"        if (bottomCSVs[i]>0.46){"+"\n"+"        anti_tag=0;"+"\n"+"      }"+"\n"+"      }"+"\n"+"    return anti_tag;"+"}",
                        

#"""
   

#std::vector<float> PDF_RMS(""" + stringforPDFs+""", """+stringforPDFs_new+ """,bool DoMCDataWeights_ttbaronly){
    #std::vector<float> PDFweights;
    #std::vector<float> PDFweights_new;
    #std::vector<float> PDFweights_refac;
    #std::vector<float> res;
    #float RMSmean=0.0;
    #float RMSerror=0.0;
    #"""+stringforPDFs3_refac+"""
    #"""+stringforPDFs2+"""
    #"""+stringforPDFs2_new+"""
    #"""+stringforPDFs2_refac+"""
    
    
    #for(int i=0; i<PDFweights.size(); i++){
        #RMSmean+=PDFweights[i]*PDFweights[i]*PDFweights_new[i]*PDFweights_new[i]*PDFweights_refac[i]*PDFweights_refac[i];
    #}
    #RMSmean=sqrt(RMSmean/float(PDFweights.size()));
    #for(int i=0; i<PDFweights.size(); i++){
        #RMSerror+=(RMSmean-PDFweights[i]*PDFweights_new[i]*PDFweights_refac[i])*(RMSmean-PDFweights[i]*PDFweights_new[i]*PDFweights_refac[i]);      
    #}
    #RMSerror=sqrt(RMSerror/float(PDFweights.size()));
    #if (RMSmean>3.0 || RMSmean<0.0 || RMSerror>3.0 || RMSerror<0.0){ RMSmean=1.0; RMSerror=1.0; };
    #res.push_back(RMSmean);
    #res.push_back(RMSmean+RMSerror);
    #res.push_back(RMSmean-RMSerror);
    
    #return res;
#}
#"""                        
#,                        
"""
float anti_loose_btag(float const* bottomCSVs, int sizeofarray){
    float anti_tag=1;
    for (int i=0; i<sizeofarray; i++){
        if(bottomCSVs[i]>0.46){
            //std::cout<<"bottomcsv"<<bottomCSVs[i]<<endl;
            //anti_tag=0;
        }
    }
            //std::cout<<"anti_tag"<<anti_tag<<endl;
    return anti_tag;
}
""",


#"""
#std::vector<float> smearWmassfactor(float mass, float phi, float eta){
    #std::vector<float> res;

    
    #UInt_t seed = int((phi + 10.0)*10000);
    #int warmup = int((eta + 10.0)*100);
    
   
    #TRandom3 myrandom=TRandom3(seed);
    
    #for (int i=0; i<warmup; i++){
        #myrandom.Gaus(0.0,7.99);
    #}
    
    #float randomnumber=myrandom.Gaus(0.0,7.99/82.0);
    #res.push_back(1+sqrt(1.23*1.23 -1.0)*randomnumber);
    #res.push_back(1+sqrt((1.23+0.18)*(1.23+0.18) -1.0)*randomnumber);
    #res.push_back(1+sqrt((1.23-0.18)*(1.23-0.18) -1.0)*randomnumber);

    
    
    #return res;

#}
#"""
#,

"""

#include "TGraph.h"
#include "TGraphErrors.h"




std::vector<float> interpolateSFandSFerrors(TGraphErrors const& SF_Function, float x_value, bool x_value_filled){
    float deltax_min=9999999999;
    float res_y=0.0;
    float res_deltayup=0.0;
    float res_deltaydown=0.0;
    int i_x=0; 
    std::vector<float> res;
    if (x_value<0.001 || x_value_filled==false)
    {
        res.push_back(0.0);
        res.push_back(0.0);
        res.push_back(0.0);
        return res;
    } else
    {
        for(int i=0; i<SF_Function.GetN();i++){
            float deltax_temp=abs(x_value-SF_Function.GetX()[i]);
            if(deltax_min>deltax_temp){
                deltax_min=deltax_temp;
                i_x=i;
            }
        }
        //std::cout<<"i_x=  "<<i_x<<endl;
        //if(i_x==0 || i_x==SF_Function.GetN() || (SF_Function.GetX()[i_x]-x_value)==0){
            //res.push_back(SF_Function.GetY()[i_x]);
            //res.push_back(SF_Function.GetErrorYhigh(i_x));
            //res.push_back(SF_Function.GetErrorYlow(i_x));
        //}else if(!(i_x==0 || i_x==SF_Function.GetN()) && (SF_Function.GetX()[i_x]-x_value)>0){
            //res.push_back((SF_Function.GetY()[i_x]-SF_Function.GetY()[i_x-1])/(SF_Function.GetX()[i_x]-SF_Function.GetX()[i_x-1])*(x_value-SF_Function.GetX()[i_x-1])+SF_Function.GetY()[i_x-1]);
            //res.push_back((SF_Function.GetErrorYhigh(i_x)-SF_Function.GetErrorYhigh(i_x-1))/(SF_Function.GetX()[i_x]-SF_Function.GetX()[i_x-1])*(x_value-SF_Function.GetX()[i_x-1])+SF_Function.GetErrorYhigh(i_x-1));
            //res.push_back((SF_Function.GetErrorYlow(i_x)-SF_Function.GetErrorYlow(i_x-1))/(SF_Function.GetX()[i_x]-SF_Function.GetX()[i_x-1])*(x_value-SF_Function.GetX()[i_x-1])+SF_Function.GetErrorYlow(i_x-1));
        //}else if(!(i_x==0 || i_x==SF_Function.GetN()) && (SF_Function.GetX()[i_x]-x_value)<0){
            //res.push_back((SF_Function.GetY()[i_x+1]-SF_Function.GetY()[i_x])/(SF_Function.GetX()[i_x+1]-SF_Function.GetX()[i_x])*(x_value-SF_Function.GetX()[i_x])+SF_Function.GetY()[i_x]);
            //res.push_back((SF_Function.GetErrorYhigh(i_x+1)-SF_Function.GetErrorYhigh(i_x))/(SF_Function.GetX()[i_x+1]-SF_Function.GetX()[i_x])*(x_value-SF_Function.GetX()[i_x])+SF_Function.GetErrorYhigh(i_x));
            //res.push_back((SF_Function.GetErrorYlow(i_x+1)-SF_Function.GetErrorYlow(i_x))/(SF_Function.GetX()[i_x+1]-SF_Function.GetX()[i_x])*(x_value-SF_Function.GetX()[i_x])+SF_Function.GetErrorYlow(i_x));
        //}
        res.push_back(SF_Function.GetY()[i_x]);
        res.push_back(SF_Function.GetErrorYhigh(i_x));
        res.push_back(SF_Function.GetErrorYlow(i_x));
    
    
        return res;    
    }
    //std::cout<<"xvalue: "<<x_value<<"  SF"<<res[0]<<endl;
}
""",
"""
std::vector<float> bbarportionweight(int const N){
    std::vector<float> res;
    
    if(N>0){
        res.push_back(1.0);
        res.push_back(1.5);
        res.push_back(0.5);
        res.push_back(0.0);
    } else {
        res.push_back(1.0);
        res.push_back(1.0);
        res.push_back(1.0);
        res.push_back(1.0);
    };
    return res;
}
  
""",

"""
int ABCD_Category(float const* Zprimes_ABCD""" +  radi + """_M, float const* Tprimes_ABCD""" +  radi + """_M, float const* Tops_ABCD""" +  radi + """_maxsubjetCSVv2, float const* Ws_ABCD""" +  radi + """_MSD, float const* Ws_ABCD""" +  radi + """_corrL2L3, float const* Tops_ABCD""" +  radi + """_MSD, float const* Tops_ABCD""" +  radi + """_corrL2L3, float const* Tops_ABCD""" +  radi + """_t32, float const* Bottoms_ABCD""" +  radi + """_CSV, float const* Ws_ABCD""" +  radi + """_t21, float const* Ws_ABCD""" + radi + """_Pt, float const* Tops_ABCD""" + radi + """_Pt, float const* Bottoms_ABCD""" + radi + """_Pt, float Evt_HT_Jets, int N_Zprime_ABCD""" + radi + """, float N_Jets, float N_packedPatJetsAK8PF""" +  radi + """){

    int res=0;
    for (int i=0; i<N_Zprime_ABCD""" +  radi + """; i++){
        if ("""+ generalselection_i +"""){
            if("""+ plotselection_topsubjetCSVv2_i +"""){
                if("""+ cut1_i +"""){
                    if("""+ cut2_i + """){
                        if(""" + cut3_i + """){
                            res=1;
                            break;
                        }
                        if(""" + cut3_anti_i + """){
                            res=2;
                            break;
                        }
                    }
                    if("""+ cut2_anti_i + """){
                        if(""" + cut3_i + """){
                            res=3;
                            break;
                        }
                        if(""" + cut3_anti_i + """){
                            res=4;
                            break;
                        }
                    }                
                }
                if("""+ cut1_anti_i +"""){
                    if("""+ cut2_i + """){
                        if(""" + cut3_i + """){
                            res=5;
                            break;
                        }
                        if(""" + cut3_anti_i + """){
                            res=6;
                            break;
                        }
                    }
        
                    if("""+ cut2_anti_i + """){
                        if(""" + cut3_i + """){
                            res=7;
                            break;
                        }
                        if(""" + cut3_anti_i + """){
                            res=8;
                            break;
                        }
                    }                
                }
            } else {
                if("""+ cut1_i +"""){
                    if("""+ cut2_i + """){
                        if(""" + cut3_i + """){
                            res=9;
                            break;
                        }
                        if(""" + cut3_anti_i + """){
                            res=10;
                            break;
                        }
                    }
                    if("""+ cut2_anti_i + """){
                        if(""" + cut3_i + """){
                            res=11;
                            break;
                        }
                        if(""" + cut3_anti_i + """){
                            res=12;
                            break;
                        }
                    }                
                }
                if("""+ cut1_anti_i +"""){
                    if("""+ cut2_i + """){
                        if(""" + cut3_i + """){
                            res=13;
                            break;
                        }
                        if(""" + cut3_anti_i + """){
                            res=14;
                            break;
                        }
                    }
                    if("""+ cut2_anti_i + """){
                        if(""" + cut3_i + """){
                            res=15;
                            break;
                        }
                        if(""" + cut3_anti_i + """){
                            res=16;
                            break;
                        }
                    }                
                }
            }
        }
    }
    return res;
}
""",

#"""
#std::vector<float> ABCD_Category_WJetMassScale(float const* Zprimes_ABCD""" +  radi + """_M, float const* Tprimes_ABCD""" +  radi + """_M, float const* Tops_ABCD""" +  radi + """_maxsubjetCSVv2, float const* Topsubjets_ABCD""" + radi + """_WeightCSVnominal, float const* Ws_ABCD""" +  radi + """_MSD, float const* Ws_ABCD""" +  radi + """_corrL2L3, float const* Tops_ABCD""" +  radi + """_MSD, float const* Tops_ABCD""" +  radi + """_corrL2L3, float const* Tops_ABCD""" +  radi + """_t32, float const* Bottoms_ABCD""" +  radi + """_CSV, float const* Bottoms_ABCD""" + radi + """_WeightCSVnominal, float const* Ws_ABCD""" +  radi + """_t21, float const* Ws_ABCD""" + radi + """_Pt, float const* Tops_ABCD""" + radi + """_Pt, float const* Bottoms_ABCD""" + radi + """_Pt){

    #std::vector<float> res;

    #float resup=0;
    #float resdown=0;
    
    #float CSVnominal=1.0;
    
   
    #float toptagnominal=1.0;

    
    #float Wtag_tag_nominal=1.0;

    

    #res.push_back(resup);
    #res.push_back(resdown);
    #res.push_back(CSVnominal*toptagnominal*Wtag_tag_nominal);
    
#}
#""",

"""
std::vector<float> CSV_weights_""" + ABCDversion + """(float const* Zprimes_ABCD""" + radi + """_M, float const* Tprimes_ABCD""" + radi + """_M, float const* Tops_ABCD""" + radi + """_maxsubjetCSVv2, float const* Ws_ABCD""" + radi + """_MSD, float const* Ws_ABCD""" + radi + """_corrL2L3, float const* Tops_ABCD""" + radi + """_MSD, float const* Tops_ABCD""" + radi + """_corrL2L3, float const* Tops_ABCD""" + radi + """_t32, float const* Bottoms_ABCD""" + radi + """_CSV, float const* Ws_ABCD""" + radi + """_t21, float const* Ws_ABCD""" + radi + """_Pt, float const* Tops_ABCD""" + radi + """_Pt, float const* Bottoms_ABCD""" + radi + """_Pt, float Evt_HT_Jets, int N_Zprime_ABCD""" + radi + """, float N_Jets, float N_packedPatJetsAK8PF""" +  radi + """, float const* Bottoms_ABCD""" + radi + """_WeightCSVnominal, float const* Bottoms_ABCD""" + radi + """_WeightCSVLFup, float const* Bottoms_ABCD""" + radi + """_WeightCSVLFdown, float const* Bottoms_ABCD""" + radi + """_WeightCSVHFup, float const* Bottoms_ABCD""" + radi + """_WeightCSVHFdown, float const* Bottoms_ABCD""" + radi + """_WeightCSVHFStats1up, float const* Bottoms_ABCD""" + radi + """_WeightCSVHFStats1down, float const* Bottoms_ABCD""" + radi + """_WeightCSVLFStats1up, float const* Bottoms_ABCD""" + radi + """_WeightCSVLFStats1down, float const* Bottoms_ABCD""" + radi + """_WeightCSVHFStats2up, float const* Bottoms_ABCD""" + radi + """_WeightCSVHFStats2down, float const* Bottoms_ABCD""" + radi + """_WeightCSVLFStats2up, float const* Bottoms_ABCD""" + radi + """_WeightCSVLFStats2down, float const* Bottoms_ABCD""" + radi + """_WeightCSVCErr1up, float const* Bottoms_ABCD""" + radi + """_WeightCSVCErr1down, float const* Bottoms_ABCD""" + radi + """_WeightCSVCErr2up, float const* Bottoms_ABCD""" + radi + """_WeightCSVCErr2down, float const* Topsubjets_ABCD""" + radi + """_WeightCSVnominal, float const* Topsubjets_ABCD""" + radi + """_WeightCSVLFup, float const* Topsubjets_ABCD""" + radi + """_WeightCSVLFdown, float const* Topsubjets_ABCD""" + radi + """_WeightCSVHFup, float const* Topsubjets_ABCD""" + radi + """_WeightCSVHFdown, float const* Topsubjets_ABCD""" + radi + """_WeightCSVHFStats1up, float const* Topsubjets_ABCD""" + radi + """_WeightCSVHFStats1down, float const* Topsubjets_ABCD""" + radi + """_WeightCSVLFStats1up, float const* Topsubjets_ABCD""" + radi + """_WeightCSVLFStats1down, float const* Topsubjets_ABCD""" + radi + """_WeightCSVHFStats2up, float const* Topsubjets_ABCD""" + radi + """_WeightCSVHFStats2down, float const* Topsubjets_ABCD""" + radi + """_WeightCSVLFStats2up, float const* Topsubjets_ABCD""" + radi + """_WeightCSVLFStats2down, float const* Topsubjets_ABCD""" + radi + """_WeightCSVCErr1up, float const* Topsubjets_ABCD""" + radi + """_WeightCSVCErr1down, float const* Topsubjets_ABCD""" + radi + """_WeightCSVCErr2up, float const* Topsubjets_ABCD""" + radi + """_WeightCSVCErr2down  ){
    std::vector<float> weights;
    
    float CSVnominal=1.0;
    float CSVLFup=1.0;
    float CSVLFdown=1.0;
    float CSVHFup=1.0;
    float CSVHFdown=1.0;
    float CSVHFStats1up=1.0;
    float CSVHFStats1down=1.0;
    float CSVLFStats1up=1.0;
    float CSVLFStats1down=1.0;
    float CSVHFStats2up=1.0;
    float CSVHFStats2down=1.0;
    float CSVLFStats2up=1.0;
    float CSVLFStats2down=1.0;
    float CSVCErr1up=1.0;
    float CSVCErr1down=1.0;
    float CSVCErr2up=1.0;
    float CSVCErr2down=1.0;

    float tpt=0.0;
    float Wpt=0.0;
    float bpt=0.0;

    for (int i=0; i<N_Zprime_ABCD""" + radi + """; i++){
        if ("""+ generalselection_i +""" && Bottoms_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0){   
            if (Bottoms_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVnominal *= Bottoms_ABCD""" + radi + """_WeightCSVnominal[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVLFup[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVLFup[i]<=1000){
                CSVLFup *= Bottoms_ABCD""" + radi + """_WeightCSVLFup[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVLFdown[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVLFdown[i]<=1000){
                CSVLFdown *= Bottoms_ABCD""" + radi + """_WeightCSVLFdown[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVHFup[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVHFup[i]<=1000){
                CSVHFup *= Bottoms_ABCD""" + radi + """_WeightCSVHFup[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVHFdown[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVHFdown[i]<=1000){
                CSVHFdown *= Bottoms_ABCD""" + radi + """_WeightCSVHFdown[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVHFStats1up[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVHFStats1up[i]<=1000){
                CSVHFStats1up *= Bottoms_ABCD""" + radi + """_WeightCSVHFStats1up[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVHFStats1down[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVHFStats1down[i]<=1000){
                CSVHFStats1down *= Bottoms_ABCD""" + radi + """_WeightCSVHFStats1down[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVLFStats1up[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVLFStats1up[i]<=1000){
                CSVLFStats1up *= Bottoms_ABCD""" + radi + """_WeightCSVLFStats1up[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVLFStats1down[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVLFStats1down[i]<=1000){
                CSVLFStats1down *= Bottoms_ABCD""" + radi + """_WeightCSVLFStats1down[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVHFStats2up[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVHFStats2up[i]<=1000){
                CSVHFStats2up *= Bottoms_ABCD""" + radi + """_WeightCSVHFStats2up[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVHFStats2down[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVHFStats2down[i]<=1000){
                CSVHFStats2down *= Bottoms_ABCD""" + radi + """_WeightCSVHFStats2down[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVLFStats2up[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVLFStats2up[i]<=1000){
                CSVLFStats2up *= Bottoms_ABCD""" + radi + """_WeightCSVLFStats2up[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVLFStats2down[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVLFStats2down[i]<=1000){
                CSVLFStats2down *= Bottoms_ABCD""" + radi + """_WeightCSVLFStats2down[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVCErr1up[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVCErr1up[i]<=1000){
                CSVCErr1down *= Bottoms_ABCD""" + radi + """_WeightCSVCErr1up[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVCErr1down[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVCErr1down[i]<=1000){
                CSVCErr1down *= Bottoms_ABCD""" + radi + """_WeightCSVCErr1down[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVCErr2up[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVCErr2up[i]<=1000){
                CSVCErr2up *= Bottoms_ABCD""" + radi + """_WeightCSVCErr2up[i];
            }
            if (Bottoms_ABCD""" + radi + """_WeightCSVCErr2down[i]>=0 && Bottoms_ABCD""" + radi + """_WeightCSVCErr2down[i]<=1000){
                CSVCErr2down *= Bottoms_ABCD""" + radi + """_WeightCSVCErr2down[i];
            }
            
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVnominal *= Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVLFup *= Topsubjets_ABCD""" + radi + """_WeightCSVLFup[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVLFdown *= Topsubjets_ABCD""" + radi + """_WeightCSVLFdown[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVHFup *= Topsubjets_ABCD""" + radi + """_WeightCSVHFup[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVHFdown *= Topsubjets_ABCD""" + radi + """_WeightCSVHFdown[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVHFStats1up *= Topsubjets_ABCD""" + radi + """_WeightCSVHFStats1up[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVHFStats1down *= Topsubjets_ABCD""" + radi + """_WeightCSVHFStats1down[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVLFStats1up *= Topsubjets_ABCD""" + radi + """_WeightCSVLFStats1up[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVLFStats1down *= Topsubjets_ABCD""" + radi + """_WeightCSVLFStats1down[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVHFStats2up *= Topsubjets_ABCD""" + radi + """_WeightCSVHFStats2up[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVHFStats2down *= Topsubjets_ABCD""" + radi + """_WeightCSVHFStats2down[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVLFStats2up *= Topsubjets_ABCD""" + radi + """_WeightCSVLFStats2up[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVLFStats2down *= Topsubjets_ABCD""" + radi + """_WeightCSVLFStats2down[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVCErr1down *= Topsubjets_ABCD""" + radi + """_WeightCSVCErr1up[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVCErr1down *= Topsubjets_ABCD""" + radi + """_WeightCSVCErr1down[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVCErr2up *= Topsubjets_ABCD""" + radi + """_WeightCSVCErr2up[i];
            }
            if (Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]>=0 && Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i]<=1000){
                CSVCErr2down *= Topsubjets_ABCD""" + radi + """_WeightCSVCErr2down[i];
            }
            break;
        }
    };
    
    weights.push_back(CSVnominal);
    weights.push_back(CSVLFup);
    weights.push_back(CSVLFdown);
    weights.push_back(CSVHFup);
    weights.push_back(CSVHFdown);
    weights.push_back(CSVHFStats1up);
    weights.push_back(CSVHFStats1down);
    weights.push_back(CSVLFStats1up);
    weights.push_back(CSVLFStats1down);
    weights.push_back(CSVHFStats2up);
    weights.push_back(CSVHFStats2down);
    weights.push_back(CSVLFStats2up);
    weights.push_back(CSVLFStats2down);
    weights.push_back(CSVCErr1up);
    weights.push_back(CSVCErr1down);
    weights.push_back(CSVCErr2up);
    weights.push_back(CSVCErr2down);    
    
    return weights;
}

"""
,

"""
std::vector<float> toptag_weights_""" + ABCDversion + """(float const* Zprimes_ABCD""" + radi + """_M, float const* Tprimes_ABCD""" + radi + """_M, float const* Tops_ABCD""" + radi + """_maxsubjetCSVv2, float const* Ws_ABCD""" + radi + """_MSD, float const* Ws_ABCD""" + radi + """_corrL2L3, float const* Tops_ABCD""" + radi + """_MSD, float const* Tops_ABCD""" + radi + """_corrL2L3, float const* Tops_ABCD""" + radi + """_t32, float const* Bottoms_ABCD""" + radi + """_CSV, float const* Ws_ABCD""" + radi + """_t21, float const* Ws_ABCD""" + radi + """_Pt, float const* Tops_ABCD""" + radi + """_Pt, float const* Bottoms_ABCD""" + radi + """_Pt, float Evt_HT_Jets, int N_Zprime_ABCD""" + radi + """, float N_Jets, float N_packedPatJetsAK8PF""" +  radi + """, float const* Tops_ABCD""" + radi + """_real, float const* Tops_ABCD""" + radi + """_matcheddecays){
    std::vector<float> weights;
    
    float toptagnominal=1.0;
    float toptagup=1.0;
    float toptagdown=1.0;
    
    float topmisstagnominal=1.0;
    float topmisstagup=1.0;
    float topmisstagdown=1.0;
    
    float SF_top_tau32_MSD_=""" + MCSF_top_t32_MSD + """;
    float SF_top_tau32_MSD_up=""" + MCSF_top_t32_MSD_up + """;
    float SF_top_tau32_MSD_down=""" + MCSF_top_t32_MSD_down + """;
    float SF_top_tau32_MSDanti_=""" + MCSF_top_t32_MSD_down + """;
    float SF_top_tau32_MSDanti_up=""" + MCSF_top_t32_MSD_up + """;
    float SF_top_tau32_MSDanti_down=""" + MCSF_top_t32_MSD_down + """;
    float SF_top_tau32anti_MSD_=""" + MCSF_top_t32_MSD + """;
    float SF_top_tau32anti_MSD_up=""" + MCSF_top_t32_MSD_up + """;
    float SF_top_tau32anti_MSD_down=""" + MCSF_top_t32_MSD_down + """;
    float SF_top_tau32anti_MSDanti_=""" + MCSF_top_t32_MSD + """;
    float SF_top_tau32anti_MSDanti_up=""" + MCSF_top_t32_MSD_up + """;
    float SF_top_tau32anti_MSDanti_down=""" + MCSF_top_t32_MSD_down + """;
    
    float SF_topmiss_tau32_MSD_=""" + MCSF_topmiss_t32_MSD + """;
    float SF_topmiss_tau32_MSD_up=""" + MCSF_topmiss_t32_MSD_up + """;
    float SF_topmiss_tau32_MSD_down=""" + MCSF_topmiss_t32_MSD_down + """;
    float SF_topmiss_tau32_MSDanti_=""" + MCSF_topmiss_t32_MSDanti + """;
    float SF_topmiss_tau32_MSDanti_up=""" + MCSF_topmiss_t32_MSDanti_up + """;
    float SF_topmiss_tau32_MSDanti_down=""" + MCSF_topmiss_t32_MSDanti_down + """;
    float SF_topmiss_tau32anti_MSD_=""" + MCSF_topmiss_t32anti_MSD + """;
    float SF_topmiss_tau32anti_MSD_up=""" + MCSF_topmiss_t32anti_MSD_up + """;
    float SF_topmiss_tau32anti_MSD_down=""" + MCSF_topmiss_t32anti_MSD_down + """;
    float SF_topmiss_tau32anti_MSDanti_=""" + MCSF_topmiss_t32anti_MSDanti + """;
    float SF_topmiss_tau32anti_MSDanti_up=""" + MCSF_topmiss_t32anti_MSDanti_up + """;
    float SF_topmiss_tau32anti_MSDanti_down=""" + MCSF_topmiss_t32anti_MSDanti_down + """;
    
    
    for (int i=0; i<N_Zprime_ABCD""" + radi + """; i++){
        if (""" + generalselection_i + """){
            //if(Tops_ABCD""" + radi + """_real[i]==1 && Tops_ABCD""" + radi + """_matcheddecays[i]>2){
            if(Tops_ABCD""" + radi + """_real[i]==1){
                if(""" + plotselection_tau32_i + """ && """ + plotselection_t_MSD_i + """){
                    toptagnominal *= SF_top_tau32_MSD_;
                    toptagup *= (SF_top_tau32_MSD_ + SF_top_tau32_MSD_up);
                    toptagdown *= (SF_top_tau32_MSD_ - SF_top_tau32_MSD_down);
                }
                if(""" + plotselection_tau32_anti_i + """ && """ + plotselection_t_MSD_i + """){
                    toptagnominal *= SF_top_tau32anti_MSD_;
                    toptagup *= (SF_top_tau32anti_MSD_ + SF_top_tau32anti_MSD_up);
                    toptagdown *= (SF_top_tau32anti_MSD_ - SF_top_tau32anti_MSD_down);
                }
                if(""" + plotselection_tau32_i + """ && """ + plotselection_t_MSD_anti_i + """){
                    toptagnominal *= SF_top_tau32_MSDanti_;
                    toptagup *= (SF_top_tau32_MSDanti_ + SF_top_tau32_MSDanti_up);
                    toptagdown *= (SF_top_tau32_MSDanti_ - SF_top_tau32_MSDanti_down);
                }
                if(""" + plotselection_tau32_anti_i + """ && """ + plotselection_t_MSD_anti_i + """){
                    toptagnominal *= SF_top_tau32anti_MSDanti_;
                    toptagup *= (SF_top_tau32anti_MSDanti_ + SF_top_tau32anti_MSDanti_up);
                    toptagdown *= (SF_top_tau32anti_MSDanti_ - SF_top_tau32anti_MSDanti_down);
                }
            } else {
                if(""" + plotselection_tau32_i + """ && """ + plotselection_t_MSD_i + """){
                    topmisstagnominal *= SF_topmiss_tau32_MSD_;
                    topmisstagup *= (SF_topmiss_tau32_MSD_ + SF_topmiss_tau32_MSD_up);
                    topmisstagdown *= (SF_topmiss_tau32_MSD_ - SF_topmiss_tau32_MSD_down);
                }
                if(""" + plotselection_tau32_anti_i + """ && """ + plotselection_t_MSD_i + """){
                    topmisstagnominal *= SF_topmiss_tau32anti_MSD_;
                    topmisstagup *= (SF_topmiss_tau32anti_MSD_ + SF_topmiss_tau32anti_MSD_up);
                    topmisstagdown *= (SF_topmiss_tau32anti_MSD_ - SF_topmiss_tau32anti_MSD_down);
                }
                if(""" + plotselection_tau32_i + """ && """ + plotselection_t_MSD_anti_i + """){
                    topmisstagnominal *= SF_topmiss_tau32_MSDanti_;
                    topmisstagup *= (SF_topmiss_tau32_MSDanti_ + SF_topmiss_tau32_MSDanti_up);
                    topmisstagdown *= (SF_topmiss_tau32_MSDanti_ - SF_topmiss_tau32_MSDanti_down);
                }
                if(""" + plotselection_tau32_anti_i + """ && """ + plotselection_t_MSD_anti_i + """){
                    topmisstagnominal *= SF_topmiss_tau32anti_MSDanti_;
                    topmisstagup *= (SF_topmiss_tau32anti_MSDanti_ + SF_topmiss_tau32anti_MSDanti_up);
                    topmisstagdown *= (SF_topmiss_tau32anti_MSDanti_ - SF_topmiss_tau32anti_MSDanti_down);
                }
            }
            break;
        }
    }
    
    weights.push_back(toptagnominal);
    weights.push_back(toptagup);
    weights.push_back(toptagdown);
    weights.push_back(topmisstagnominal);
    weights.push_back(topmisstagup);
    weights.push_back(topmisstagdown);
   
        
    return weights;
}

"""
,
"""
std::vector<float> Wtag_weights_""" + ABCDversion + """(float const* Zprimes_ABCD""" + radi + """_M, float const* Tprimes_ABCD""" + radi + """_M, float const* Tops_ABCD""" + radi + """_maxsubjetCSVv2, float const* Ws_ABCD""" + radi + """_MSD, float const* Ws_ABCD""" + radi + """_corrL2L3, float const* Tops_ABCD""" + radi + """_MSD, float const* Tops_ABCD""" + radi + """_corrL2L3, float const* Tops_ABCD""" + radi + """_t32, float const* Bottoms_ABCD""" + radi + """_CSV, float const* Ws_ABCD""" + radi + """_t21, float const* Ws_ABCD""" + radi + """_Pt, float const* Tops_ABCD""" + radi + """_Pt, float const* Bottoms_ABCD""" + radi + """_Pt, float Evt_HT_Jets, int N_Zprime_ABCD""" + radi + """, float N_Jets, float N_packedPatJetsAK8PF""" +  radi + """, float const* Ws_ABCD""" + radi + """_real, float const* Ws_ABCD""" + radi + """_matcheddecays){
    std::vector<float> weights;
    
    float Wtag_tag_nominal=1.0;
    float Wtag_tag_up=1.0;
    float Wtag_tag_down=1.0;

    
    float SF_W_tau21_MSD=""" + MCSF_W_t21_MSD + """;
    float SF_W_tau21_MSD_up=""" + MCSF_W_t21_MSD_up + """;
    float SF_W_tau21_MSD_down=""" + MCSF_W_t21_MSD_down + """;
    float SF_W_tau21_MSDanti=""" + MCSF_W_t21_MSDanti + """;
    float SF_W_tau21_MSDanti_up=""" + MCSF_W_t21_MSDanti_up + """;
    float SF_W_tau21_MSDanti_down=""" + MCSF_W_t21_MSDanti_down + """;
    float SF_W_tau21anti_MSD=""" + MCSF_W_t21anti_MSD + """;
    float SF_W_tau21anti_MSD_up=""" + MCSF_W_t21anti_MSD_up + """;
    float SF_W_tau21anti_MSD_down=""" + MCSF_W_t21anti_MSD_down + """;
    float SF_W_tau21anti_MSDanti=""" + MCSF_W_t21anti_MSDanti + """;
    float SF_W_tau21anti_MSDanti_up=""" + MCSF_W_t21anti_MSDanti_up + """;
    float SF_W_tau21anti_MSDanti_down=""" + MCSF_W_t21anti_MSDanti_down + """;
    
    //float SF_Wmiss_tau21_MSD=""" + MCSF_Wmiss_t21_MSD + """;
    //float SF_Wmiss_tau21_MSD_up=""" + MCSF_Wmiss_t21_MSD_up + """;
    //float SF_Wmiss_tau21_MSD_down=""" + MCSF_Wmiss_t21_MSD_down + """;
    //float SF_Wmiss_tau21_MSDanti=""" + MCSF_Wmiss_t21_MSDanti + """;
    //float SF_Wmiss_tau21_MSDanti_up=""" + MCSF_Wmiss_t21_MSDanti_up + """;
    //float SF_Wmiss_tau21_MSDanti_down=""" + MCSF_Wmiss_t21_MSDanti_down + """;
    //float SF_Wmiss_tau21anti_MSD=""" + MCSF_Wmiss_t21anti_MSD + """;
    //float SF_Wmiss_tau21anti_MSD_up=""" + MCSF_Wmiss_t21anti_MSD_up + """;
    //float SF_Wmiss_tau21anti_MSD_down=""" + MCSF_Wmiss_t21anti_MSD_down + """;
    //float SF_Wmiss_tau21anti_MSDanti=""" + MCSF_Wmiss_t21anti_MSDanti + """;
    //float SF_Wmiss_tau21anti_MSDanti_up=""" + MCSF_Wmiss_t21anti_MSDanti_up + """;
    //float SF_Wmiss_tau21anti_MSDanti_down=""" + MCSF_Wmiss_t21anti_MSDanti_down + """;    
    

    for (int i=0; i<N_Zprime_ABCD""" + radi + """; i++){
        if ("""+ generalselection_i + """ ){
                if(""" + plotselection_W_tau21_i + """ && """ + plotselection_W_MSD_i + """){
                    Wtag_tag_nominal *= SF_W_tau21_MSD;
                    Wtag_tag_up *= ((SF_W_tau21_MSD + SF_W_tau21_MSD_up)+0.041*log(Ws_ABCD""" + radi + """_Pt[i]/200.0));
                    Wtag_tag_down *= ((SF_W_tau21_MSD - SF_W_tau21_MSD_down)-0.041*log(Ws_ABCD""" + radi + """_Pt[i]/200.0));
                    break;
                }
                if(""" + plotselection_W_tau21_anti_i + """ && """ + plotselection_W_MSD_i + """){
                    Wtag_tag_nominal *= SF_W_tau21anti_MSD;
                    Wtag_tag_up *= ((SF_W_tau21anti_MSD - SF_W_tau21anti_MSD_up)-0.054*log(Ws_ABCD""" + radi + """_Pt[i]/200.0));
                    Wtag_tag_down *= ((SF_W_tau21anti_MSD + SF_W_tau21anti_MSD_down)+0.054*log(Ws_ABCD""" + radi + """_Pt[i]/200.0));
                    break;
                }
                if(""" + plotselection_W_tau21_i + """ && """ + plotselection_W_MSD_anti_i + """){
                    Wtag_tag_nominal *= SF_W_tau21_MSDanti;
                    Wtag_tag_up *= ((SF_W_tau21_MSDanti + SF_W_tau21_MSDanti_up)+0.041*log(Ws_ABCD""" + radi + """_Pt[i]/200.0));
                    Wtag_tag_down *= ((SF_W_tau21_MSDanti - SF_W_tau21_MSDanti_down)-0.041*log(Ws_ABCD""" + radi + """_Pt[i]/200.0));
                    break;
                }
                if(""" + plotselection_W_tau21_anti_i + """ && """ + plotselection_W_MSD_anti_i + """){
                    Wtag_tag_nominal *= SF_W_tau21anti_MSDanti;
                    Wtag_tag_up *= ((SF_W_tau21anti_MSDanti - SF_W_tau21anti_MSDanti_up)-0.054*log(Ws_ABCD""" + radi + """_Pt[i]/200.0));
                    Wtag_tag_down *= ((SF_W_tau21anti_MSDanti + SF_W_tau21anti_MSDanti_down)+0.054*log(Ws_ABCD""" + radi + """_Pt[i]/200.0));
                    break;
                }

            break;
        }
    }
    
    weights.push_back(Wtag_tag_nominal);
    weights.push_back(Wtag_tag_up);
    weights.push_back(Wtag_tag_down);
    
    
    return weights;
}

""",

"""
std::vector<float> RenFacEnv(float muR20_muF20, float muR05_muF05, float muR10_muF20 , float muR10_muF05, float muR20_muF10, float muR05_muF10, bool DoMCDataWeights_ttbaronly){
    std::vector<float> res;
    float envUp=1.0;
    float envDown=1.0;
    
        if (muR20_muF20>envUp){
            envUp=muR20_muF20*(1.29465480107*(DoMCDataWeights_ttbaronly==1)+1*(DoMCDataWeights_ttbaronly==0));
        }
        if (muR20_muF20<envDown){
            envDown=muR20_muF20*(1.29465480107*(DoMCDataWeights_ttbaronly==1)+1*(DoMCDataWeights_ttbaronly==0));
        }
        if (muR05_muF05>envUp){
            envUp=muR05_muF05*(0.755423761535*(DoMCDataWeights_ttbaronly==1)+1*(DoMCDataWeights_ttbaronly==0));
        }
        if (muR05_muF05<envDown){
            envDown=muR05_muF05*(0.755423761535*(DoMCDataWeights_ttbaronly==1)+1*(DoMCDataWeights_ttbaronly==0));
        }
        if (muR10_muF20>envUp){
            envUp=muR10_muF20*(1.07529312329*(DoMCDataWeights_ttbaronly==1)+1*(DoMCDataWeights_ttbaronly==0));
        }
        if (muR10_muF20<envDown){
            envDown=muR10_muF20*(1.07529312329*(DoMCDataWeights_ttbaronly==1)+1*(DoMCDataWeights_ttbaronly==0));
        }
        if (muR10_muF05>envUp){
            envUp=muR10_muF05*(0.926990626083*(DoMCDataWeights_ttbaronly==1)+1*(DoMCDataWeights_ttbaronly==0));
        }
        if (muR10_muF05<envDown){
            envDown=muR10_muF05*(0.926990626083*(DoMCDataWeights_ttbaronly==1)+1*(DoMCDataWeights_ttbaronly==0));
        }
        if (muR20_muF10>envUp){
            envUp=muR20_muF10*(1.12267866063*(DoMCDataWeights_ttbaronly==1)+1*(DoMCDataWeights_ttbaronly==0));
        }
        if (muR20_muF10<envDown){
            envDown=muR20_muF10*(1.12267866063*(DoMCDataWeights_ttbaronly==1)+1*(DoMCDataWeights_ttbaronly==0));
        }
        if (muR05_muF10>envUp){
            envUp=muR05_muF10*(0.814903279727*(DoMCDataWeights_ttbaronly==1)+1*(DoMCDataWeights_ttbaronly==0));
        }
        if (muR05_muF10<envDown){
            envDown=muR05_muF10*(0.814903279727*(DoMCDataWeights_ttbaronly==1)+1*(DoMCDataWeights_ttbaronly==0));
        }

    res.push_back(envUp);
    res.push_back(envDown);
    
    return res;
}
"""

"""
std::vector<float> ABCD_syts(float const* Zprimes_ABCD""" +  radi + """_M, float const* Tprimes_ABCD""" +  radi + """_M, float const* Tops_ABCD""" +  radi + """_maxsubjetCSVv2, float const* Ws_ABCD""" +  radi + """_MSD, float const* Ws_ABCD""" +  radi + """_corrL2L3, float const* Tops_ABCD""" +  radi + """_MSD, float const* Tops_ABCD""" +  radi + """_corrL2L3, float const* Tops_ABCD""" +  radi + """_t32, float const* Bottoms_ABCD""" +  radi + """_CSV, float const* Ws_ABCD""" +  radi + """_t21, float const* Ws_ABCD""" + radi + """_Pt, float const* Tops_ABCD""" + radi + """_Pt, float const* Bottoms_ABCD""" + radi + """_Pt, float Evt_HT_Jets, int N_Zprime_ABCD""" + radi + """, float N_Jets, float N_packedPatJetsAK8PF""" +  radi + """){
    std::vector<float> res;
    float ABCD_rateUp=1.0;
    float ABCD_rateDown=1.0;
    float ABCD_shapeUp=1.0;
    float ABCD_shapeDown=1.0;
    
    for (int i=0; i<N_Zprime_ABCD""" + radi + """; i++){
        if ("""+ generalselection_i +"""){
            if("""+ plotselection_topsubjetCSVv2_i +"""){
                ABCD_rateUp=(1.0 + (""" + str(Zprime_withtopbtag_systrate) + """));
                ABCD_rateDown=(1.0 - (""" + str(Zprime_withtopbtag_systrate) + """));
                ABCD_shapeUp=(1.0+(Zprimes_ABCD""" +  radi + """_M[i]-1970.0) * (""" + str(Zprime_withtopbtag_systshape_m) + """));
                ABCD_shapeDown=(1.0-(Zprimes_ABCD""" +  radi + """_M[i]-1970.0) * (""" + str(Zprime_withtopbtag_systshape_m) + """));
            } else {
                ABCD_rateUp=(1.0 + (""" + str(Zprime_notopbtag_systrate) + """));
                ABCD_rateDown=(1.0 - (""" + str(Zprime_notopbtag_systrate) + """));
                //ABCD_shapeUp=(((Zprimes_ABCD""" +  radi + """_M[i]) * (""" + str(Zprime_notopbtag_systshape_m) + """) + (""" + str(Zprime_notopbtag_systshape_c) + """)));
                //ABCD_shapeDown=(-((Zprimes_ABCD""" +  radi + """_M[i]) * (""" + str(Zprime_notopbtag_systshape_m) + """) + (""" + str(Zprime_notopbtag_systshape_c) + """)));
                ABCD_shapeUp=(1.0+(Zprimes_ABCD""" +  radi + """_M[i]-2000.0) * (""" + str(Zprime_notopbtag_systshape_m) + """));
                ABCD_shapeDown=(1.0-(Zprimes_ABCD""" +  radi + """_M[i]-2000.0) * (""" + str(Zprime_notopbtag_systshape_m) + """));
            };
        break;
        };
    }
    res.push_back(ABCD_rateUp);
    res.push_back(ABCD_rateDown);
    res.push_back(ABCD_shapeUp);
    res.push_back(ABCD_shapeDown);
    
    return res;
}
""",


"""
std::vector<float> CSV_weights_all(float const* Zprimes_ABCD""" + radi + """_M, float const* Tprimes_ABCD""" + radi + """_M, float const* Tops_ABCD""" + radi + """_maxsubjetCSVv2, float const* Ws_ABCD""" + radi + """_MSD, float const* Ws_ABCD""" + radi + """_corrL2L3, float const* Tops_ABCD""" + radi + """_MSD, float const* Tops_ABCD""" + radi + """_corrL2L3, float const* Tops_ABCD""" + radi + """_t32, float const* Bottoms_ABCD""" + radi + """_CSV, float const* Ws_ABCD""" + radi + """_t21, float const* Ws_ABCD""" + radi + """_Pt, float const* Tops_ABCD""" + radi + """_Pt, float const* Bottoms_ABCD""" + radi + """_Pt, float Evt_HT_Jets, int N_Zprime_ABCD""" + radi + """, float N_Jets, float N_packedPatJetsAK8PF""" +  radi + """, float const* Bottoms_ABCD""" + radi + """_WeightCSVnominal, float const* Bottoms_ABCD""" + radi + """_WeightCSVLFup, float const* Bottoms_ABCD""" + radi + """_WeightCSVLFdown, float const* Bottoms_ABCD""" + radi + """_WeightCSVHFup, float const* Bottoms_ABCD""" + radi + """_WeightCSVHFdown, float const* Bottoms_ABCD""" + radi + """_WeightCSVHFStats1up, float const* Bottoms_ABCD""" + radi + """_WeightCSVHFStats1down, float const* Bottoms_ABCD""" + radi + """_WeightCSVLFStats1up, float const* Bottoms_ABCD""" + radi + """_WeightCSVLFStats1down, float const* Bottoms_ABCD""" + radi + """_WeightCSVHFStats2up, float const* Bottoms_ABCD""" + radi + """_WeightCSVHFStats2down, float const* Bottoms_ABCD""" + radi + """_WeightCSVLFStats2up, float const* Bottoms_ABCD""" + radi + """_WeightCSVLFStats2down, float const* Bottoms_ABCD""" + radi + """_WeightCSVCErr1up, float const* Bottoms_ABCD""" + radi + """_WeightCSVCErr1down, float const* Bottoms_ABCD""" + radi + """_WeightCSVCErr2up, float const* Bottoms_ABCD""" + radi + """_WeightCSVCErr2down, float const* Topsubjets_ABCD""" + radi + """_WeightCSVnominal, float const* Topsubjets_ABCD""" + radi + """_WeightCSVLFup, float const* Topsubjets_ABCD""" + radi + """_WeightCSVLFdown, float const* Topsubjets_ABCD""" + radi + """_WeightCSVHFup, float const* Topsubjets_ABCD""" + radi + """_WeightCSVHFdown, float const* Topsubjets_ABCD""" + radi + """_WeightCSVHFStats1up, float const* Topsubjets_ABCD""" + radi + """_WeightCSVHFStats1down, float const* Topsubjets_ABCD""" + radi + """_WeightCSVLFStats1up, float const* Topsubjets_ABCD""" + radi + """_WeightCSVLFStats1down, float const* Topsubjets_ABCD""" + radi + """_WeightCSVHFStats2up, float const* Topsubjets_ABCD""" + radi + """_WeightCSVHFStats2down, float const* Topsubjets_ABCD""" + radi + """_WeightCSVLFStats2up, float const* Topsubjets_ABCD""" + radi + """_WeightCSVLFStats2down, float const* Topsubjets_ABCD""" + radi + """_WeightCSVCErr1up, float const* Topsubjets_ABCD""" + radi + """_WeightCSVCErr1down, float const* Topsubjets_ABCD""" + radi + """_WeightCSVCErr2up, float const* Topsubjets_ABCD""" + radi + """_WeightCSVCErr2down  ){
    std::vector<float> weights;
    
    float CSVnominal=1.0;
    float CSVLFup=1.0;
    float CSVLFdown=1.0;
    float CSVHFup=1.0;
    float CSVHFdown=1.0;
    float CSVHFStats1up=1.0;
    float CSVHFStats1down=1.0;
    float CSVLFStats1up=1.0;
    float CSVLFStats1down=1.0;
    float CSVHFStats2up=1.0;
    float CSVHFStats2down=1.0;
    float CSVLFStats2up=1.0;
    float CSVLFStats2down=1.0;
    float CSVCErr1up=1.0;
    float CSVCErr1down=1.0;
    float CSVCErr2up=1.0;
    float CSVCErr2down=1.0;

    float tpt=0.0;
    float Wpt=0.0;
    float bpt=0.0;

    for (int i=0; i<N_Zprime_ABCD""" + radi + """; i++){
        if ( Evt_HT_Jets>1000 && Bottoms_ABCD""" + radi + """_WeightCSVnominal[i]>(-0.5)){         
            CSVnominal *= Bottoms_ABCD""" + radi + """_WeightCSVnominal[i];
            CSVLFup *= Bottoms_ABCD""" + radi + """_WeightCSVLFup[i];
            CSVLFdown *= Bottoms_ABCD""" + radi + """_WeightCSVLFdown[i];
            CSVHFup *= Bottoms_ABCD""" + radi + """_WeightCSVHFup[i];
            CSVHFdown *= Bottoms_ABCD""" + radi + """_WeightCSVHFdown[i];
            CSVHFStats1up *= Bottoms_ABCD""" + radi + """_WeightCSVHFStats1up[i];
            CSVHFStats1down *= Bottoms_ABCD""" + radi + """_WeightCSVHFStats1down[i];
            CSVLFStats1up *= Bottoms_ABCD""" + radi + """_WeightCSVLFStats1up[i];
            CSVLFStats1down *= Bottoms_ABCD""" + radi + """_WeightCSVLFStats1down[i];
            CSVHFStats2up *= Bottoms_ABCD""" + radi + """_WeightCSVHFStats2up[i];
            CSVHFStats2down *= Bottoms_ABCD""" + radi + """_WeightCSVHFStats2down[i];
            CSVLFStats2up *= Bottoms_ABCD""" + radi + """_WeightCSVLFStats2up[i];
            CSVLFStats2down *= Bottoms_ABCD""" + radi + """_WeightCSVLFStats2down[i];
            CSVCErr1down *= Bottoms_ABCD""" + radi + """_WeightCSVCErr1up[i];
            CSVCErr1down *= Bottoms_ABCD""" + radi + """_WeightCSVCErr1down[i];
            CSVCErr2up *= Bottoms_ABCD""" + radi + """_WeightCSVCErr2up[i];
            CSVCErr2down *= Bottoms_ABCD""" + radi + """_WeightCSVCErr2down[i];
            
            CSVnominal *= Topsubjets_ABCD""" + radi + """_WeightCSVnominal[i];
            CSVLFup *= Topsubjets_ABCD""" + radi + """_WeightCSVLFup[i];
            CSVLFdown *= Topsubjets_ABCD""" + radi + """_WeightCSVLFdown[i];
            CSVHFup *= Topsubjets_ABCD""" + radi + """_WeightCSVHFup[i];
            CSVHFdown *= Topsubjets_ABCD""" + radi + """_WeightCSVHFdown[i];
            CSVHFStats1up *= Topsubjets_ABCD""" + radi + """_WeightCSVHFStats1up[i];
            CSVHFStats1down *= Topsubjets_ABCD""" + radi + """_WeightCSVHFStats1down[i];
            CSVLFStats1up *= Topsubjets_ABCD""" + radi + """_WeightCSVLFStats1up[i];
            CSVLFStats1down *= Topsubjets_ABCD""" + radi + """_WeightCSVLFStats1down[i];
            CSVHFStats2up *= Topsubjets_ABCD""" + radi + """_WeightCSVHFStats2up[i];
            CSVHFStats2down *= Topsubjets_ABCD""" + radi + """_WeightCSVHFStats2down[i];
            CSVLFStats2up *= Topsubjets_ABCD""" + radi + """_WeightCSVLFStats2up[i];
            CSVLFStats2down *= Topsubjets_ABCD""" + radi + """_WeightCSVLFStats2down[i];
            CSVCErr1down *= Topsubjets_ABCD""" + radi + """_WeightCSVCErr1up[i];
            CSVCErr1down *= Topsubjets_ABCD""" + radi + """_WeightCSVCErr1down[i];
            CSVCErr2up *= Topsubjets_ABCD""" + radi + """_WeightCSVCErr2up[i];
            CSVCErr2down *= Topsubjets_ABCD""" + radi + """_WeightCSVCErr2down[i];
                        
        }
    };
    
    weights.push_back(CSVnominal);
    weights.push_back(CSVLFup);
    weights.push_back(CSVLFdown);
    weights.push_back(CSVHFup);
    weights.push_back(CSVHFdown);
    weights.push_back(CSVHFStats1up);
    weights.push_back(CSVHFStats1down);
    weights.push_back(CSVLFStats1up);
    weights.push_back(CSVLFStats1down);
    weights.push_back(CSVHFStats2up);
    weights.push_back(CSVHFStats2down);
    weights.push_back(CSVLFStats2up);
    weights.push_back(CSVLFStats2down);
    weights.push_back(CSVCErr1up);
    weights.push_back(CSVCErr1down);
    weights.push_back(CSVCErr2up);
    weights.push_back(CSVCErr2down);    
    
    return weights;
}

"""
,
"""float triggerresult(int Triggered_HLT_PFHT800_vX, int Triggered_HLT_PFHT900_vX, int Triggered_HLT_PFJet450_vX, float Prescale_HLT_PFHT800_vX, float Prescale_HLT_PFHT900_vX,float Prescale_HLT_PFJet450_vX){
    int result=0;
    if(Triggered_HLT_PFHT800_vX==1 || Triggered_HLT_PFHT900_vX==1 || Triggered_HLT_PFJet450_vX){result=1.0;}; //run H has damaged PFHT900 GeV
    return result;
}
"""

]




additionalobjectsfromaddtionalrootfile=[
    
"""



  TFile* SFfile = new TFile("/nfs/dust/cms/user/skudella/pyroot-plotscripts/Zprime_SBSSSFs_Graphs.root","READONLY");
  TGraphErrors* QCDMadgraph_Graph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M=(TGraphErrors*)SFfile->Get("Graph_QCDMadgraph_SB_SF_bottom_anti_Zprime_M");
  TGraphErrors* QCDMadgraph_Graph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt=(TGraphErrors*)SFfile->Get("Graph_QCDMadgraph_SB_SF_bottom_anti_Tops_Pt");
  TGraphErrors* QCDMadgraph_Graph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt=(TGraphErrors*)SFfile->Get("Graph_QCDMadgraph_SB_SF_top_anti_Tops_Pt");
  TGraphErrors* QCDMadgraph_Graph_SF_SB_top_anti_Signal_Topfirst_Ws_Pt=(TGraphErrors*)SFfile->Get("Graph_QCDMadgraph_SB_SF_top_anti_Ws_Pt");
  TGraphErrors* QCDPythia8_Graph_SF_SB_bottom_anti_Signal_Topfirst_Zprime_M=(TGraphErrors*)SFfile->Get("Graph_QCDPythia8_SB_SF_bottom_anti_Zprime_M");
  TGraphErrors* QCDPythia8_Graph_SF_SB_bottom_anti_Signal_Topfirst_Tops_Pt=(TGraphErrors*)SFfile->Get("Graph_QCDPythia8_SB_SF_bottom_anti_Tops_Pt");
  TGraphErrors* QCDPythia8_Graph_SF_SB_top_anti_Signal_Topfirst_Tops_Pt=(TGraphErrors*)SFfile->Get("Graph_QCDPythia8_SB_SF_top_anti_Tops_Pt");
  TGraphErrors* QCDPythia8_Graph_SF_SB_top_anti_Signal_Topfirst_Ws_Pt=(TGraphErrors*)SFfile->Get("Graph_QCDPythia8_SB_SF_top_anti_Ws_Pt");
  
  TGraphErrors* QCDMadgraph_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M=(TGraphErrors*)SFfile->Get("Graph_QCDMadgraph_SB_SF_withtopbtag_bottom_anti_Zprime_M");
  TGraphErrors* QCDMadgraph_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt=(TGraphErrors*)SFfile->Get("Graph_QCDMadgraph_SB_SF_withtopbtag_bottom_anti_Tops_Pt");
  TGraphErrors* QCDMadgraph_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt=(TGraphErrors*)SFfile->Get("Graph_QCDMadgraph_SB_SF_withtopbtag_top_anti_Tops_Pt");
  TGraphErrors* QCDMadgraph_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt=(TGraphErrors*)SFfile->Get("Graph_QCDMadgraph_SB_SF_withtopbtag_top_anti_Ws_Pt");
  TGraphErrors* QCDPythia8_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Zprime_M=(TGraphErrors*)SFfile->Get("Graph_QCDPythia8_SB_SF_withtopbtag_bottom_anti_Zprime_M");
  TGraphErrors* QCDPythia8_Graph_SF_SB_withtopbtag_bottom_anti_Signal_Topfirst_Tops_Pt=(TGraphErrors*)SFfile->Get("Graph_QCDPythia8_SB_SF_withtopbtag_bottom_anti_Tops_Pt");
  TGraphErrors* QCDPythia8_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Tops_Pt=(TGraphErrors*)SFfile->Get("Graph_QCDPythia8_SB_SF_withtopbtag_top_anti_Tops_Pt");
  TGraphErrors* QCDPythia8_Graph_SF_SB_top_withbtag_anti_Signal_Topfirst_Ws_Pt=(TGraphErrors*)SFfile->Get("Graph_QCDPythia8_SB_SF_withtopbtag_top_anti_Ws_Pt");
  
  
  SFfile->cd();
  
"""
    
    ]


additionalvariables=[
			
                        
                        'ABCD_CatID:=1.0 * ABCD_Category(Zprimes_ABCD' + radi + '_M,   Tprimes_ABCD' + radi + '_M,   Tops_ABCD' + radi + '_maxsubjetCSVv2,   Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3,   Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3,   Tops_ABCD' + radi + '_t32,   Bottoms_ABCD' + radi + '_CSV,   Ws_ABCD' + radi + '_t21, Ws_ABCD' + radi + '_Pt, Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt, Evt_HT_Jets, N_Zprime_ABCD' + radi + ', N_Jets, N_packedPatJetsAK8PF' +  radi + ')',
                        
                        'ABCD_rate_systUp:=ABCD_syts( Zprimes_ABCD' +  radi + '_M,  Tprimes_ABCD' +  radi + '_M,  Tops_ABCD' +  radi + '_maxsubjetCSVv2,  Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3,  Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3,  Tops_ABCD' +  radi + '_t32,  Bottoms_ABCD' +  radi + '_CSV,  Ws_ABCD' +  radi + '_t21,  Ws_ABCD' + radi + '_Pt,  Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt,  Evt_HT_Jets,  N_Zprime_ABCD' + radi + ',  N_Jets,  N_packedPatJetsAK8PF' +  radi + ')[0]',
                        'ABCD_rate_systDown:=ABCD_syts( Zprimes_ABCD' +  radi + '_M,  Tprimes_ABCD' +  radi + '_M,  Tops_ABCD' +  radi + '_maxsubjetCSVv2,  Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3,  Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3,  Tops_ABCD' +  radi + '_t32,  Bottoms_ABCD' +  radi + '_CSV,  Ws_ABCD' +  radi + '_t21,  Ws_ABCD' + radi + '_Pt,  Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt,  Evt_HT_Jets,  N_Zprime_ABCD' + radi + ',  N_Jets,  N_packedPatJetsAK8PF' +  radi + ')[1]',
                        
                        'ABCD_shape_systUp:=ABCD_syts( Zprimes_ABCD' +  radi + '_M,  Tprimes_ABCD' +  radi + '_M,  Tops_ABCD' +  radi + '_maxsubjetCSVv2,  Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3,  Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3,  Tops_ABCD' +  radi + '_t32,  Bottoms_ABCD' +  radi + '_CSV,  Ws_ABCD' +  radi + '_t21,  Ws_ABCD' + radi + '_Pt,  Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt,  Evt_HT_Jets,  N_Zprime_ABCD' + radi + ',  N_Jets,  N_packedPatJetsAK8PF' +  radi + ')[2]',
                        'ABCD_shape_systDown:=ABCD_syts( Zprimes_ABCD' +  radi + '_M,  Tprimes_ABCD' +  radi + '_M,  Tops_ABCD' +  radi + '_maxsubjetCSVv2,  Ws_ABCD' + radi + '_MSD, Ws_ABCD' + radi + '_corrL2L3,  Tops_ABCD' + radi + '_MSD, Tops_ABCD' + radi + '_corrL2L3,  Tops_ABCD' +  radi + '_t32,  Bottoms_ABCD' +  radi + '_CSV,  Ws_ABCD' +  radi + '_t21,  Ws_ABCD' + radi + '_Pt,  Tops_ABCD' + radi + '_Pt,  Bottoms_ABCD' + radi + '_Pt,  Evt_HT_Jets,  N_Zprime_ABCD' + radi + ',  N_Jets,  N_packedPatJetsAK8PF' +  radi + ')[3]',                         
                        
                        'ABCD_CatA_withtopbtag:=1',
                        'ABCD_CatB_withtopbtag:=2',
                        'ABCD_CatC_withtopbtag:=3',
                        'ABCD_CatD_withtopbtag:=4',
                        'ABCD_CatE_withtopbtag:=5',
                        'ABCD_CatF_withtopbtag:=6',
                        'ABCD_CatG_withtopbtag:=7',
                        'ABCD_CatH_withtopbtag:=8',
                        
                        'ABCD_CatA_notopbtag:=9',
                        'ABCD_CatB_notopbtag:=10',
                        'ABCD_CatC_notopbtag:=11',
                        'ABCD_CatD_notopbtag:=12',
                        'ABCD_CatE_notopbtag:=13',
                        'ABCD_CatF_notopbtag:=14',
                        'ABCD_CatG_notopbtag:=15',
                        'ABCD_CatH_notopbtag:=16',
                        
                  
                        
                        'triggered:=triggerresult(Triggered_HLT_PFHT800_vX, Triggered_HLT_PFHT900_vX, Triggered_HLT_PFJet450_vX, Prescale_HLT_PFHT800_vX, Prescale_HLT_PFHT900_vX, Prescale_HLT_PFJet450_vX)',

]

