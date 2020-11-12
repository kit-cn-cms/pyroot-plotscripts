#include "../interface/EventFilter.h"
// Event filter to be used with CSV files

const std::string WHITESPACE = " \n\r\t\f\v";

std::string ltrim(const std::string &s)
{
  size_t start = s.find_first_not_of(WHITESPACE);
  return (start == std::string::npos) ? "" : s.substr(start);
}

std::string rtrim(const std::string &s)
{
  size_t end = s.find_last_not_of(WHITESPACE);
  return (end == std::string::npos) ? "" : s.substr(0, end + 1);
}

std::string trim(const std::string &s)
{
  return rtrim(ltrim(s));
}

// for string delimiter
std::vector<std::string> EventFilter::split(string s, string delimiter)
{
  size_t pos_start = 0, pos_end, delim_len = delimiter.length();
  std::string token;
  std::vector<string> res;

  while ((pos_end = s.find(delimiter, pos_start)) != string::npos)
  {
    token = s.substr(pos_start, pos_end - pos_start);
    pos_start = pos_end + delim_len;
    res.push_back(token);
  }

  res.push_back(s.substr(pos_start));
  return res;
}

EventFilter::EventFilter(std::vector<std::string> filenames)
{

  listLength = 0;
  nEventsFiltered = 0;

  TString dump = "";
  char comma;

  int count = 0;
  bool readline = true;
  bool readTitle = false;
  long run;
  long lumi;
  long evt;
  std::string line;
  // TString line;

  for (auto &filename : filenames)
  {
    std::vector<long> vec_run;
    std::vector<long> vec_lumi;
    std::vector<long> vec_evt;
    if (filename != "" and filename != "NONE")
    {
      std::ifstream eventList(filename);
      std::cout << "reading Event list to be filtered from " << filename << std::endl;

      vec_run.clear();
      vec_lumi.clear();
      vec_evt.clear();
      if (eventList.is_open())
      {
        while (getline(eventList, line))
        {
          // std::cout << line << '\n';
          count++;
          std::vector<std::string> v = split(line, ",");
          if (v[0] == "run")
            continue;
          // std::cout<<v[0]<<" "<<v[1]<<" "<< v[2] <<std::endl;
          vec_run.push_back(std::stol(trim(v[0])));
          vec_lumi.push_back(std::stol(trim(v[1])));
          vec_evt.push_back(std::stol(trim(v[2])));
        }
        eventList.close();
      }
      std::cout << "done reading the event filter list" << std::endl;
      std::cout << vec_run.size() << " " << vec_lumi.size() << " " << vec_evt.size() << " " << std::endl;
      listLength = vec_run.size();
    }
    std::vector<std::vector<long>> vv;
    vv.push_back(vec_run);
    vv.push_back(vec_lumi);
    vv.push_back(vec_evt);
    VetoMap[filename] = vv;
    vec_run.clear();
    vec_lumi.clear();
    vec_evt.clear();
  }
  std::cout << "---------------" << '\n';
  for (const auto &p : VetoMap)
  {
    // std::cout << "m[" << p.first << "] = " << p.second << '\n';
    std::cout << p.first << '\n';
    // for (const auto &v : p.second)
    // {
    //   for (const auto &elem : v)
    //   {
    //     std::cout << elem << '\n';
    //   }
    // }
  }
  std::cout << "---------------" << '\n';
}

bool EventFilter::KeepEvent(std::string file, Long64_t Evt_Run, Long64_t Evt_Lumi, Long64_t Evt_ID)
{
  // bool eventToBeKept=true;
  // for(int i=0; i<listLength; i++){
  //   if(vec_run.at(i)==Evt_Run and vec_lumi.at(i)==Evt_Lumi and vec_evt.at(i)==Evt_ID){
  //     eventToBeKept=false;
  //     break;
  //   }
  // }
  // if(eventToBeKept==false){nEventsFiltered++;}
  // return eventToBeKept;
  // std::cout << "---------------" << '\n';
  // for (const auto &p : VetoMap)
  // {
  //   // std::cout << "m[" << p.first << "] = " << p.second << '\n';
  //   std::cout << p.first << '\n';
  // }
  // std::cout << file << std::endl;
  // std::cout << "---------------" << '\n';
  // for (const auto &v : VetoMap[file])
  // {
  //   for (const auto &elem : v)
  //   {
  //     std::cout << elem << '\n';
  //   }
  // }
  // std::cout << "---------------" << '\n';

  bool eventToBeKept = true;
  std::vector<std::vector<long>> events = VetoMap[file];
  std::vector<long> vec_run = events.at(0);
  std::vector<long> vec_lumi = events.at(1);
  std::vector<long> vec_evt = events.at(2);
  listLength = vec_run.size();
  // std::cout << listLength << std::endl;
  for (int i = 0; i < listLength; i++)
  {
    if (vec_run.at(i) == Evt_Run and vec_lumi.at(i) == Evt_Lumi and vec_evt.at(i) == Evt_ID)
    {
      eventToBeKept = false;
      break;
    }
  }
  if (eventToBeKept == false)
  {
    nEventsFiltered++;
  }
  return eventToBeKept;
}

int EventFilter::GetNFiltered()
{
  return nEventsFiltered;
}