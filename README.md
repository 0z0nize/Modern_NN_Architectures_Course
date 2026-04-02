# [🧠 Modern Neural Network Architectures Course](https://github.com/itmo-cv-lab/modern-nn-architectures-course)

A comprehensive course on modern neural network architectures, covering the evolution from classical CNNs to advanced Transformers, diffusion models, and state-of-the-art generative AI.

## 📚 Course Lectures

### [🧠 Lecture 1: Convolutional Neural Networks](https://github.com/0z0nize/Modern_NN_Architectures_Course/blob/main/Shkarovskiy_1.ipynb)
This lecture explores the evolution of convolutional neural networks from the pioneering LeNet (1990) to the state-of-the-art EfficientNet (2019). We'll dive deep into the architectural innovations, design principles, and breakthroughs that shaped modern CNN development over three decades.

### [🔄 Lecture 2: Transformers Basic](https://github.com/0z0nize/Modern_NN_Architectures_Course/blob/main/Shkarovskiy_2.ipynb)
This lecture introduces the revolutionary Transformer architecture that has transformed the field of natural language processing and beyond. We'll explore tokenization, Byte Pair Encoding (BPE), positional encoding, and dive deep into the architecture of Transformers, BERT, and GPT models, including parameter scaling discussions.

### [🚀 Lecture 3: Transformers Advanced](https://github.com/0z0nize/Modern_NN_Architectures_Course/blob/main/Shkarovskiy_3.ipynb)
This lecture explores advanced concepts in modern Transformer architectures and how they drive today's large language models. We'll cover Scaling Laws, inference optimization techniques (KV-cache, speculative decoding), architectural innovations (GQA/MQA, sliding-window, sparse attention, Mixture of Experts), and parameter-efficient fine-tuning methods like LoRA.

### [🎨 Lecture 4: Generative Computer Vision Basic](https://github.com/0z0nize/Modern_NN_Architectures_Course/blob/main/Shkarovskiy_4.ipynb)
This lecture explores the fundamental theory of generative models and their classification based on density approximation approaches. We'll examine how generative models are categorized into three main types: those that compute density directly (ARMs), those that approximate it using ELBO (VAE, Diffusion Models), and those that don't rely on density estimation (GANs). The lecture covers ARMs (Pixel CNN), GANs (including WGAN and Earth Mover's Distance), and VAEs (Bayesian Framework, ELBO, Reparameterization Trick).

### 🌊 Lecture 5: Diffusion Models
This lecture explores diffusion models — one of the most powerful approaches to generative modeling in modern computer vision. We'll dive deep into the theoretical foundations of diffusion processes, covering model training procedures, the Diffusion Transformer (DiT) architecture, and applications in video generation.

### [🔗 Lecture 6: Multimodal Architecture](https://github.com/0z0nize/Modern_NN_Architectures_Course/blob/main/Shkarovskiy_6.ipynb)
This lecture explores multimodal neural network architectures that can process and understand both visual and textual information simultaneously. We'll dive deep into CLIP (Contrastive Language-Image Pre-training) and BLIP (Bootstrapping Language-Image Pre-training) models, covering their architectures, training procedures, and applications in image-text retrieval, zero-shot classification, image captioning, and visual question answering.

### [🎯 Lecture 7: Efficient Deep Learning — Quantization, Pruning & Distillation](https://github.com/0z0nize/Modern_NN_Architectures_Course/blob/main/Shkarovskiy_7.ipynb)
This lecture explores essential model compression and optimization techniques for deploying large neural networks efficiently. We'll cover Quantization (number formats FP32/FP16/INT8, linear quantization, PTQ vs QAT, AWQ/GPTQ/GGUF), Pruning (magnitude pruning, iterative pruning), Knowledge Distillation (teacher-student frameworks, feature-based and relation-based distillation), and Mixed Precision Training (FP16 with FP32 master weights, 30–50% VRAM savings). These techniques are critical for deploying LLMs on limited resources, reducing inference costs, and working with mobile and edge devices.
