// Event filter to be used with CSV files
class EventFilter {
   public:
    EventFilter(std::string filename);
    ~EventFilter();
    bool KeepEvent(Long64_t Evt_Run, Long64_t Evt_Lumi, Long64_t Evt_ID);
    int  GetNFiltered();

   private:
    std::vector< long > vec_run;
    std::vector< long > vec_lumi;
    std::vector< long > vec_evt;
    int                 listLength;
    int                 nEventsFiltered;
};

EventFilter::EventFilter(std::string filename)
{
    listLength      = 0;
    nEventsFiltered = 0;

    std::ifstream eventList(filename);
    TString       dump = "";
    char          comma;

    int  count     = 0;
    bool readline  = true;
    bool readTitle = false;
    long run;
    long lumi;
    long evt;

    if (filename != "" and filename != "NONE") {
        std::cout << "reading Event list to be filtered" << std::endl;

        eventList >> dump;
        eventList >> dump;
        while (eventList >> run >> comma >> lumi >> comma >> evt) {
            count++;
            std::cout << count << std::endl;
            std::cout << comma << std::endl;
            std::cout << run << " " << lumi << " " << evt << std::endl;
            vec_run.push_back(run);
            vec_lumi.push_back(lumi);
            vec_evt.push_back(evt);
        }

        eventList.close();
        std::cout << "done reading the event filter list" << std::endl;
        std::cout << vec_run.size() << " " << vec_lumi.size() << " " << vec_evt.size() << " " << std::endl;
        listLength = vec_run.size();
    }
}

bool EventFilter::KeepEvent(Long64_t Evt_Run, Long64_t Evt_Lumi, Long64_t Evt_ID)
{
    bool eventToBeKept = true;
    for (int i = 0; i < listLength; i++) {
        if (vec_run.at(i) == Evt_Run and vec_lumi.at(i) == Evt_Lumi and vec_evt.at(i) == Evt_ID) {
            eventToBeKept = false;
            break;
        }
    }
    if (eventToBeKept == false) { nEventsFiltered++; }
    return eventToBeKept;
}

int EventFilter::GetNFiltered() { return nEventsFiltered; }
