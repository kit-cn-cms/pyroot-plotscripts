class ttbarsysthelper {
   public:
    ttbarsysthelper();
    ~ttbarsysthelper();
    float GetISRScaleFactorUp(int& ttbar_subprocess, int& njets);
    float GetISRScaleFactorDown(int& ttbar_subprocess, int& njets);
    float GetFSRScaleFactorUp(int& ttbar_subprocess, int& njets);
    float GetFSRScaleFactorDown(int& ttbar_subprocess, int& njets);
    float GetHDAMPScaleFactorUp(int& ttbar_subprocess, int& njets);
    float GetHDAMPScaleFactorDown(int& ttbar_subprocess, int& njets);
    float GetUEScaleFactorUp(int& ttbar_subprocess, int& njets);
    float GetUEScaleFactorDown(int& ttbar_subprocess, int& njets);
    int   GetTtbarSubProcess(int& GenEvt_I_TTPlusCC, int& GenEvt_I_TTPlusBB);

   private:
    // int is number of jets and float the corresponding scale factor
    std::map< std::pair< int, int >, float > ISRUp;
    std::map< std::pair< int, int >, float > ISRDown;
    std::map< std::pair< int, int >, float > FSRUp;
    std::map< std::pair< int, int >, float > FSRDown;
    std::map< std::pair< int, int >, float > HDAMPUp;
    std::map< std::pair< int, int >, float > HDAMPDown;
    std::map< std::pair< int, int >, float > UEUp;
    std::map< std::pair< int, int >, float > UEDown;
};

ttbarsysthelper::ttbarsysthelper()
{
    // first number in pair: 0->ttlf,1->ttcc,2->ttb,3->tt2b,4->ttbb
    // second number in pair: njets
    ISRUp[std::pair< int, int >(0, 4)] = 0.987;
    ISRUp[std::pair< int, int >(0, 5)] = 1.007;
    ISRUp[std::pair< int, int >(0, 6)] = 1.062;
    ISRUp[std::pair< int, int >(1, 4)] = 1.013;
    ISRUp[std::pair< int, int >(1, 5)] = 1.013;
    ISRUp[std::pair< int, int >(1, 6)] = 1.078;
    ISRUp[std::pair< int, int >(2, 4)] = 1.016;
    ISRUp[std::pair< int, int >(2, 5)] = 1.025;
    ISRUp[std::pair< int, int >(2, 6)] = 1.09;
    ISRUp[std::pair< int, int >(3, 4)] = 0.932;
    ISRUp[std::pair< int, int >(3, 5)] = 1.025;
    ISRUp[std::pair< int, int >(3, 6)] = 1.055;
    ISRUp[std::pair< int, int >(4, 4)] = 1.024;
    ISRUp[std::pair< int, int >(4, 5)] = 1.02;
    ISRUp[std::pair< int, int >(4, 6)] = 1.074;

    ISRDown[std::pair< int, int >(0, 4)] = 1.006;
    ISRDown[std::pair< int, int >(0, 5)] = 0.969;
    ISRDown[std::pair< int, int >(0, 6)] = 0.929;
    ISRDown[std::pair< int, int >(1, 4)] = 0.969;
    ISRDown[std::pair< int, int >(1, 5)] = 0.958;
    ISRDown[std::pair< int, int >(1, 6)] = 0.91;
    ISRDown[std::pair< int, int >(2, 4)] = 0.982;
    ISRDown[std::pair< int, int >(2, 5)] = 0.973;
    ISRDown[std::pair< int, int >(2, 6)] = 0.902;
    ISRDown[std::pair< int, int >(3, 4)] = 1.024;
    ISRDown[std::pair< int, int >(3, 5)] = 0.977;
    ISRDown[std::pair< int, int >(3, 6)] = 0.936;
    ISRDown[std::pair< int, int >(4, 4)] = 0.967;
    ISRDown[std::pair< int, int >(4, 5)] = 0.948;
    ISRDown[std::pair< int, int >(4, 6)] = 0.888;

    FSRUp[std::pair< int, int >(0, 4)] = 0.817;
    FSRUp[std::pair< int, int >(0, 5)] = 0.765;
    FSRUp[std::pair< int, int >(0, 6)] = 0.75;
    FSRUp[std::pair< int, int >(1, 4)] = 1.061;
    FSRUp[std::pair< int, int >(1, 5)] = 1.013;
    FSRUp[std::pair< int, int >(1, 6)] = 1.023;
    FSRUp[std::pair< int, int >(2, 4)] = 1.018;
    FSRUp[std::pair< int, int >(2, 5)] = 1.015;
    FSRUp[std::pair< int, int >(2, 6)] = 1.01;
    FSRUp[std::pair< int, int >(3, 4)] = 1.067;
    FSRUp[std::pair< int, int >(3, 5)] = 1.031;
    FSRUp[std::pair< int, int >(3, 6)] = 1.067;
    FSRUp[std::pair< int, int >(4, 4)] = 1.024;
    FSRUp[std::pair< int, int >(4, 5)] = 1.019;
    FSRUp[std::pair< int, int >(4, 6)] = 1.06;

    FSRDown[std::pair< int, int >(0, 4)] = 1.029;
    FSRDown[std::pair< int, int >(0, 5)] = 1.052;
    FSRDown[std::pair< int, int >(0, 6)] = 1.073;
    FSRDown[std::pair< int, int >(1, 4)] = 0.858;
    FSRDown[std::pair< int, int >(1, 5)] = 0.885;
    FSRDown[std::pair< int, int >(1, 6)] = 0.846;
    FSRDown[std::pair< int, int >(2, 4)] = 0.906;
    FSRDown[std::pair< int, int >(2, 5)] = 0.908;
    FSRDown[std::pair< int, int >(2, 6)] = 0.893;
    FSRDown[std::pair< int, int >(3, 4)] = 0.795;
    FSRDown[std::pair< int, int >(3, 5)] = 0.865;
    FSRDown[std::pair< int, int >(3, 6)] = 0.844;
    FSRDown[std::pair< int, int >(4, 4)] = 0.841;
    FSRDown[std::pair< int, int >(4, 5)] = 0.871;
    FSRDown[std::pair< int, int >(4, 6)] = 0.853;

    HDAMPUp[std::pair< int, int >(0, 4)] = 0.994;
    HDAMPUp[std::pair< int, int >(0, 5)] = 1.008;
    HDAMPUp[std::pair< int, int >(0, 6)] = 1.029;
    HDAMPUp[std::pair< int, int >(1, 4)] = 1.013;
    HDAMPUp[std::pair< int, int >(1, 5)] = 1.013;
    HDAMPUp[std::pair< int, int >(1, 6)] = 1.042;
    HDAMPUp[std::pair< int, int >(2, 4)] = 1.016;
    HDAMPUp[std::pair< int, int >(2, 5)] = 1.034;
    HDAMPUp[std::pair< int, int >(2, 6)] = 1.046;
    HDAMPUp[std::pair< int, int >(3, 4)] = 1.024;
    HDAMPUp[std::pair< int, int >(3, 5)] = 1.023;
    HDAMPUp[std::pair< int, int >(3, 6)] = 1.07;
    HDAMPUp[std::pair< int, int >(4, 4)] = 1.038;
    HDAMPUp[std::pair< int, int >(4, 5)] = 1.018;
    HDAMPUp[std::pair< int, int >(4, 6)] = 1.041;

    HDAMPDown[std::pair< int, int >(0, 4)] = 1.006;
    HDAMPDown[std::pair< int, int >(0, 5)] = 0.971;
    HDAMPDown[std::pair< int, int >(0, 6)] = 0.935;
    HDAMPDown[std::pair< int, int >(1, 4)] = 0.965;
    HDAMPDown[std::pair< int, int >(1, 5)] = 0.97;
    HDAMPDown[std::pair< int, int >(1, 6)] = 0.932;
    HDAMPDown[std::pair< int, int >(2, 4)] = 0.978;
    HDAMPDown[std::pair< int, int >(2, 5)] = 0.949;
    HDAMPDown[std::pair< int, int >(2, 6)] = 0.919;
    HDAMPDown[std::pair< int, int >(3, 4)] = 0.922;
    HDAMPDown[std::pair< int, int >(3, 5)] = 0.917;
    HDAMPDown[std::pair< int, int >(3, 6)] = 0.942;
    HDAMPDown[std::pair< int, int >(4, 4)] = 0.938;
    HDAMPDown[std::pair< int, int >(4, 5)] = 0.927;
    HDAMPDown[std::pair< int, int >(4, 6)] = 0.918;

    UEUp[std::pair< int, int >(0, 4)] = 0.994;
    UEUp[std::pair< int, int >(0, 5)] = 0.989;
    UEUp[std::pair< int, int >(0, 6)] = 1.003;
    UEUp[std::pair< int, int >(1, 4)] = 1.013;
    UEUp[std::pair< int, int >(1, 5)] = 1.013;
    UEUp[std::pair< int, int >(1, 6)] = 1.005;
    UEUp[std::pair< int, int >(2, 4)] = 0.984;
    UEUp[std::pair< int, int >(2, 5)] = 1.016;
    UEUp[std::pair< int, int >(2, 6)] = 1.01;
    UEUp[std::pair< int, int >(3, 4)] = 0.976;
    UEUp[std::pair< int, int >(3, 5)] = 0.977;
    UEUp[std::pair< int, int >(3, 6)] = 1.013;
    UEUp[std::pair< int, int >(4, 4)] = 0.976;
    UEUp[std::pair< int, int >(4, 5)] = 0.98;
    UEUp[std::pair< int, int >(4, 6)] = 1.01;

    UEDown[std::pair< int, int >(0, 4)] = 1.006;
    UEDown[std::pair< int, int >(0, 5)] = 1.008;
    UEDown[std::pair< int, int >(0, 6)] = 0.997;
    UEDown[std::pair< int, int >(1, 4)] = 0.974;
    UEDown[std::pair< int, int >(1, 5)] = 0.987;
    UEDown[std::pair< int, int >(1, 6)] = 0.983;
    UEDown[std::pair< int, int >(2, 4)] = 1.017;
    UEDown[std::pair< int, int >(2, 5)] = 0.984;
    UEDown[std::pair< int, int >(2, 6)] = 0.988;
    UEDown[std::pair< int, int >(3, 4)] = 1.024;
    UEDown[std::pair< int, int >(3, 5)] = 1.023;
    UEDown[std::pair< int, int >(3, 6)] = 0.987;
    UEDown[std::pair< int, int >(4, 4)] = 1.024;
    UEDown[std::pair< int, int >(4, 5)] = 1.019;
    UEDown[std::pair< int, int >(4, 6)] = 0.99;
}

ttbarsysthelper::~ttbarsysthelper()
{
    // nothing to do here
}

float ttbarsysthelper::GetISRScaleFactorUp(int& ttbar_subprocess, int& njets)
{
    return njets < 6 ? ISRUp[std::pair< int, int >(ttbar_subprocess, njets)] : ISRUp[std::pair< int, int >(ttbar_subprocess, 6)];
}
float ttbarsysthelper::GetISRScaleFactorDown(int& ttbar_subprocess, int& njets)
{
    return njets < 6 ? ISRDown[std::pair< int, int >(ttbar_subprocess, njets)] : ISRDown[std::pair< int, int >(ttbar_subprocess, 6)];
}
float ttbarsysthelper::GetFSRScaleFactorUp(int& ttbar_subprocess, int& njets)
{
    return njets < 6 ? FSRUp[std::pair< int, int >(ttbar_subprocess, njets)] : FSRUp[std::pair< int, int >(ttbar_subprocess, 6)];
}
float ttbarsysthelper::GetFSRScaleFactorDown(int& ttbar_subprocess, int& njets)
{
    return njets < 6 ? FSRDown[std::pair< int, int >(ttbar_subprocess, njets)] : FSRDown[std::pair< int, int >(ttbar_subprocess, 6)];
}
float ttbarsysthelper::GetHDAMPScaleFactorUp(int& ttbar_subprocess, int& njets)
{
    return njets < 6 ? HDAMPUp[std::pair< int, int >(ttbar_subprocess, njets)] : HDAMPUp[std::pair< int, int >(ttbar_subprocess, 6)];
}
float ttbarsysthelper::GetHDAMPScaleFactorDown(int& ttbar_subprocess, int& njets)
{
    return njets < 6 ? HDAMPDown[std::pair< int, int >(ttbar_subprocess, njets)] : HDAMPDown[std::pair< int, int >(ttbar_subprocess, 6)];
}
float ttbarsysthelper::GetUEScaleFactorUp(int& ttbar_subprocess, int& njets)
{
    return njets < 6 ? UEUp[std::pair< int, int >(ttbar_subprocess, njets)] : UEUp[std::pair< int, int >(ttbar_subprocess, 6)];
}
float ttbarsysthelper::GetUEScaleFactorDown(int& ttbar_subprocess, int& njets)
{
    return njets < 6 ? UEDown[std::pair< int, int >(ttbar_subprocess, njets)] : UEDown[std::pair< int, int >(ttbar_subprocess, 6)];
}

int ttbarsysthelper::GetTtbarSubProcess(int& GenEvt_I_TTPlusCC, int& GenEvt_I_TTPlusBB)
{
    // translate the flags available in the ntuples to the flag needed above for the ttbar subprocesses
    int i;
    if (GenEvt_I_TTPlusCC == 0 && GenEvt_I_TTPlusBB == 0) { i = 0; }
    else if (GenEvt_I_TTPlusCC == 1) {
        i = 1;
    }
    else if (GenEvt_I_TTPlusBB == 1) {
        i = 2;
    }
    else if (GenEvt_I_TTPlusBB == 2) {
        i = 3;
    }
    else if (GenEvt_I_TTPlusBB == 3) {
        i = 4;
    }
    else {
        std::cout << "!!! Error something went wrong during ttbar subprocess classification !!!" << std::endl;
        i = -1;
    }
    return i;
}
