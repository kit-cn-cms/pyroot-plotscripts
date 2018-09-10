
#include <unistd.h>
#include <iostream>
#include <vector>
#include <string>

#include <TFile.h>
#include <TH1D.h>
#include <TH1D.h>


void usage(){

}

int main(int argc,char *argv[]){


  std::vector<std::string> inputfile ;
  std::vector<std::string> histname  ;
  std::string outputfile("syst.root") ;
  std::string outhistname("");

  bool verbose = false ;

  {
    int c ;
    while(( c = getopt(argc,argv,"i:h:H:o:v")) != -1 ){
      
      switch( c){
	
      case 'i' :
	{
	  inputfile . push_back( std::string( optarg ) );
	  break;
	}
      case 'h' :
	{
	  histname . push_back( std::string ( optarg ) );
	  break;
	}
      case 'H' :
	{
	  outhistname . assign( optarg );
	  break;
	}
      case 'o' :
	{
	  outputfile . assign( optarg );
	  break ; 
	}
      case 'v' :
	{
	  verbose = true;
	  break ; 
	}
      }//end switch
    }//end while-Loop
  } //end scope.

  if( outputfile == "" ){
    usage();
    std::cout <<"[error] : output file name is empty." << std::endl ;
    return 0;
  }


  if( inputfile . size() == 1 && histname . size() == 3)
    {
      inputfile . push_back( inputfile[0] );
      inputfile . push_back( inputfile[0] );
    }
  else if( inputfile . size() == 3 && histname . size() == 1)
    {
      histname.push_back( histname[0] );
      histname.push_back( histname[0] );
    }
  else if( inputfile . size() == 3 && histname . size() == 3)
    {
    }
  else
    {
      usage ();
      return 0 ;
    }

  if( outhistname == "" ){
    std::cout<<"no outname given"<<std::endl;
    outhistname = histname[2] ;
  }

  std::cout <<std::endl ;
  std::cout <<"* Old nominal : " << inputfile[0] << ", histname " << histname[0] << std::endl ; 
  std::cout <<"* Old syst    : " << inputfile[1] << ", histname " << histname[1] << std::endl ; 
  std::cout <<"* New nominal : " << inputfile[2] << ", histname " << histname[2] << std::endl ; 
  std::cout <<"* and \n* Output file : " << outputfile << " , histname " << outhistname << std::endl ; 
  std::cout <<std::endl ;


  TFile * f_old_nom = TFile::Open( inputfile[0] .c_str() );
  TFile * f_old_sys = TFile::Open( inputfile[1] .c_str() );
  TFile * f_new_nom = TFile::Open( inputfile[2] .c_str() );

  TH1F * h_old_nom = 0;
  TH1F * h_old_sys = 0;
  TH1F * h_new_nom = 0;

  f_old_nom ->GetObject(  histname[0].c_str() ,h_old_nom );
  f_old_sys ->GetObject(  histname[1].c_str() ,h_old_sys );
  f_new_nom ->GetObject(  histname[2].c_str() ,h_new_nom );

  if( h_old_nom == 0 ){
    std::cout << "failed to obtain" <<  histname[0] << " from file " << inputfile[0] << std::endl ; 
    return 0 ;
  }
  if( h_old_sys == 0 ){
    std::cout << "failed to obtain" <<  histname[1] << " from file " << inputfile[1] << std::endl ; 
    return 0 ;
  }
  if( h_new_nom == 0 ){
    std::cout << "failed to obtain" <<  histname[2] << " from file " << inputfile[2] << std::endl ; 
    return 0 ;
  }

  if( verbose ){
    std::cout << "debug : " <<  histname[0] << " from file " << inputfile[0] << " -> Integral() = "<< h_old_nom->Integral() << std::endl ; 
    std::cout << "debug : " <<  histname[1] << " from file " << inputfile[1] << " -> Integral() = "<< h_old_sys->Integral() << std::endl ; 
    std::cout << "debug : " <<  histname[2] << " from file " << inputfile[2] << " -> Integral() = "<< h_new_nom->Integral() << std::endl ; 
  }
  
  TFile * f_out =TFile::Open( outputfile.c_str() , "update" );
  if( f_out -> IsZombie() ){
    // This may be redundunt. In case of file access failure, it crush as of the file open above.
    std::cout <<"Out put file " << outputfile << " could not be opend. Failed." << std::endl ; 
    return 0 ; 
  }

  TH1F * h_out = new TH1F( outhistname.c_str(),
			   outhistname.c_str(),
			   h_new_nom -> GetNbinsX(),
			   h_new_nom -> GetXaxis() -> GetXmin(),
			   h_new_nom -> GetXaxis() -> GetXmax() );
  
  for( unsigned int i = 0 ; i < h_out->GetNbinsX() + 1 ; i++ ){
    
    double n_old_sys = h_old_sys -> GetBinContent( i ) ;
    double n_old_nom = h_old_nom -> GetBinContent( i ) ;
    double n_new_nom = h_new_nom -> GetBinContent( i ) ;

    double weight = 1 ; 
    
    if( n_old_nom == 0 && n_old_sys != 0 ){
      std::cout <<"[warning] " << i <<"-th bin of the old-nominal histogram has no entry, while old-syst histogram has some entries.\n"
		<< "         This bin will be kept as it is in thre new-nominal histogram" << std::endl ; 
      weight = 1 ; 
    }else if( n_old_nom != 0 && n_old_sys == 0 ){ 
      std::cout <<"[warning] " << i <<"-th bin of the old-syst histogram has no entry, while old-nominal histogram has some entries.\n"
		<< "         This bin will be kept as it is in thre new-nominal histogram" << std::endl ; 
      weight = 1 ;
    }else if( n_old_nom == 0 && n_old_sys == 0 && n_new_nom == 0 ){ 
      // no warning in this case since all of the histograms have no entries in this bin.
      weight = 1 ;
    }else if( n_old_nom == 0 && n_old_sys == 0 ){ 
      std::cout <<"[warning] " << i <<"-th bin of the old-syst and old-syst histogram have no entry, while new-nominal histogram has some entries.\n"
		<< "         This bin will be kept as it is in the new-nominal histogram" << std::endl ; 
      weight = 1 ; 
    }else if( n_old_nom != 0 && n_old_sys != 0 && n_new_nom == 0 ){ 
      std::cout <<"[warning] " << i <<"-th bin of the old-syst and old-syst histogram have some entries, while new-nominal histogram has no entry.\n"
		<< "         This bin will be kept as zero." << std::endl ; 
      // just warning message. I do not care the value of weight.
    }else{
      weight = n_old_sys / n_old_nom ; 
    }

    h_out ->SetBinContent( i , n_new_nom * weight ) ; 

    if(verbose){
      std::cout << i << "-th bin of old_nom " << n_old_nom << std::endl ; 
      std::cout << i << "-th bin of old_sys " << n_old_sys << std::endl ; 
      std::cout << i << "-th bin of new_nom " << n_new_nom << std::endl ; 
      std::cout << i << "-th bin of new_syst will be " << n_new_nom * weight << std::endl ; 
    }


  } // bin-loop endes

  h_out -> Write();

  f_out->Close();

}

