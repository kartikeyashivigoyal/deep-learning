import onnx
from onnx import version_converter, helper
import click
import argparse
import onnx_graphsurgeon as gs

onnx_model = onnx.load(model_path)
gs_graph = gs.import_onnx(onnx_model)

#reference : https://github.com/NVIDIA/TensorRT/tree/master/tools/onnx-graphsurgeon

#delete node
delete_list = [
  node for node in gs_graph.nodes if node.name == delete_node_name
]
for cur_node in bad_nodes:
  print(f"-W- Deleting Node {cur_node.name} has type {cur_node.op}")
  cn_inputs = cn.inputs
  try:
    # check to see if the current node has an input
    inp_node = cn.i()
  except:
    out_node = cn.o()
