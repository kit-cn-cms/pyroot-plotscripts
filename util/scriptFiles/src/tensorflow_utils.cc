#include "../interface/tensorflow_utils.h"

tensorflow_utils::tensorflow_utils(/* args */)
{
}

tensorflow_utils::~tensorflow_utils()
{
}


std::unique_ptr<tensorflow::Session> tensorflow_utils::init_session(tensorflow::Status& status, const std::string& pathToGraph, const std::string& checkpointPath){
  auto session = std::unique_ptr<tensorflow::Session>(tensorflow::NewSession( tensorflow::SessionOptions() ));
  if( session == nullptr ) {
      throw std::runtime_error("Could not create Tensorflow session.");
      }
  // Read in protobuf we exported
  tensorflow::MetaGraphDef graph;
  status = tensorflow::ReadBinaryProto( tensorflow::Env::Default(), pathToGraph, &graph);
  if( !status.ok() ) {
      throw std::runtime_error("Status could not be read");
      }

  // Add the graph to the session
  status = session->Create( graph.graph_def() );
  if( !status.ok() ) {
      throw std::runtime_error("Error creating graph: "+status.ToString());
      }

  // Read weights from the saved checkpoint
  tensorflow::Tensor checkpointPathTensor( tensorflow::DT_STRING, tensorflow::TensorShape() );
  checkpointPathTensor.scalar<std::string>()() = checkpointPath;

  status = session->Run(
      { {graph.saver_def().filename_tensor_name(), checkpointPathTensor } }, 
      {}, 
      { graph.saver_def().restore_op_name() },
      nullptr);
  if( !status.ok() ) {
        throw std::runtime_error("Error loading checkpoint from "+checkpointPath+": "+status.ToString());
        }
       
  return session;
}

int tensorflow_utils::getMaxPosition(std::vector<tensorflow::Tensor> &output, int nClasses) {
    double max_value = -5;
    int max_pos = -1;
    for( int idim=0; idim<nClasses; idim++ ) {
        if( output.at(0).tensor<float,2>()(0,idim)> max_value ) {
            max_value = output.at(0).tensor<float,2>()(0,idim);
            max_pos = idim;
            }
        }
    return max_pos;
}