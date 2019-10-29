#ifndef EVENTFILTER
#define EVENTFILTER

#include <vector>
#include <iostream>

// Event filter to be used with CSV files
class EventFilter {

  public:
    EventFilter(std::string filename);
    ~EventFilter();
    bool KeepEvent(Long64_t Evt_Run, Long64_t Evt_Lumi, Long64_t Evt_ID);
    int GetNFiltered();

  private:
    std::vector<long> vec_run;
  std::vector<long> vec_lumi;
  std::vector<long> vec_evt;
  int listLength;
  int nEventsFiltered;

};

#endif // EVENTFILTER