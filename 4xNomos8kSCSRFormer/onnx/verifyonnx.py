import onnx

onnx_model = onnx.load("4xNomos8kSCSRFormer_131212.onnx")
onnx.checker.check_model(onnx_model)

onnx_model = onnx.load("4xNomos8kSCSRFormer_136464.onnx")
onnx.checker.check_model(onnx_model)

onnx_model = onnx.load("4xNomos8kSCSRFormer_136464_fp16.onnx")
onnx.checker.check_model(onnx_model)

onnx_model = onnx.load("4xNomos8kSCSRFormer_131212_onnxsim.onnx")
onnx.checker.check_model(onnx_model)

onnx_model = onnx.load("4xNomos8kSCSRFormer_136464_onnxsim.onnx")
onnx.checker.check_model(onnx_model)

onnx_model = onnx.load("4xNomos8kSCSRFormer_136464_fp16_onnxsim.onnx")
onnx.checker.check_model(onnx_model)

onnx_model = onnx.load("4xNomos8kSCSRFormer_131212_onnxsim_fp16.onnx")
onnx.checker.check_model(onnx_model)
