#ifndef EVENTFILTER
#define EVENTFILTER

#include <vector>
#include <iostream>

// Event filter to be used with CSV files
class EventFilter {

  public:
    EventFilter( std::vector<std::string> filenames);

    ~EventFilter();
    bool KeepEvent(std::string file, Long64_t Evt_Run, Long64_t Evt_Lumi, Long64_t Evt_ID);
    int GetNFiltered();
    std::vector<std::string> split (string s, string delimiter);

  private:
  // std::vector<long> vec_run;
  // std::vector<long> vec_lumi;
  // std::vector<long> vec_evt;
  std::map<std::string, std::vector<std::vector<long>>> VetoMap;
  int listLength;
  int nEventsFiltered;

};

#endif // EVENTFILTER