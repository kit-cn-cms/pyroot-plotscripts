#ifndef TENSORFLOW_UTILS
#define TENSORFLOW_UTILS

#include <tensorflow/core/protobuf/meta_graph.pb.h>
#include "tensorflow/core/public/session.h"
#include "tensorflow/cc/framework/ops.h"
#include "tensorflow/core/framework/tensor.h"

#include <vector>
#include <string>

class tensorflow_utils
{
private:
    /* data */
public:
    tensorflow_utils(/* args */);
    ~tensorflow_utils();

    static std::unique_ptr<tensorflow::Session> init_session(tensorflow::Status& status, const std::string& pathToGraph, const std::string& checkpointPath);
    static int getMaxPosition(std::vector<tensorflow::Tensor> &output, int nClasses);

};

#endif