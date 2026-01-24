---

title: Deep Learning Paper Reading Notes
subtitle: none
description: dl paper notes
tags: deep_learning
created: 2018-01-11
published: 2020-06-17
status: ongoing
confidence: log
importance: 1
---
## Background

Based on [Awesome Deep Learning
Papers](https://github.com/terryum/awesome-deep-learning-papers) plus my
own addition of literature summary

## Famous Machine Learning Conferences

-   [NIPS](https://nips.cc/) - general machine learning (US)
-   [ICML](https://icml.cc/) - general machine learning (international)
-   [CVPR](http://cvpr2019.thecvf.com/) - computer vision (US)
-   [ECCV](https://eccv2018.org/) - computer vision (european)
-   [ICCV](http://iccv2019.thecvf.com/submission/timeline) - computer
    vision (international)
-   [SIGGRAPH](https://www.siggraph.org/) - animation, computer graphic

## Famous Challenges / Dataset

list: <https://competitions.codalab.org/>

-   \[2010-2017\] [ImageNet](http://image-net.org/about-stats)

-   \[2005-2012\] [Pascal VOC](http://image-net.org/about-stats)

## Activity Monitoring / Recognition

Human Related

-   \(2017\) [A comprehensive review on handcrafted and learning-based
    action representation approaches for human activity
    recognition](https://www.semanticscholar.org/paper/A-comprehensive-review-on-handcrafted-and-action-Sargano-Angelov/a87e37d43d4c47bef8992ace408de0f872739efc)

Baby Related

-   \(2018\) [Computer Vision for Medical Infant Motion Analysis: State
    of the Art and RGB-D Data
    Set](http://openaccess.thecvf.com/content_eccv_2018_workshops/w31/html/Hesse_Computer_Vision_for_Medical_Infant_Motion_Analysis_State_of_the_ECCVW_2018_paper.html)

## Depth Estimation

-   \(2018\) [Evaluation of CNN-based Single-Image Depth Estimation
    Methods](https://arxiv.org/pdf/1805.01328.pdf)
    -   common criteria: (y - gt) / gt in various forms (abs, sq, sqrt,
        log, etc.)
    -   novel quality criterion, allowing for a more detailed analysis.
        -   planar consistency -- given that we have gt of wall
            orientation, we can do comparison of the diffs (dist and
            angle)
        -   edge consistency -- given we have some edge gt, can do dist
            error
        -   absolute distance accuracy -- the predicted depth in the
            plan shouldnt stray too far.
    -   [new dataset](http://www.lmf.bgu.tum.de/ibims1/) attached and
        SOTA methods evaluated.
-   \(2018\) [Revisiting Single Image Depth Estimation:Toward Higher
    Resolution Maps with Accurate Object
    Boundaries](https://arxiv.org/pdf/1803.08673.pdf)
    -   custom loss to lessen blurry-ness and more detail preservation.
        results look good.
-   \(2019\) [Monocular Depth Estimation: A
    Survey](https://arxiv.org/abs/1901.09402)
-   \(2019\) [FastDepth: Fast Monocular Depth Estimation on Embedded
    Systems](https://arxiv.org/pdf/1903.03273v1.pdf)

## Depth Fusion

-   \(2018\) [overview
    slides](https://www.slideshare.net/yuhuang/depth-fusion-from-rgb-and-depth-sensors)
-   \(2018\) [Monocular Dense Reconstruction by Depth Estimation
    Fusion](https://sci-hub.tw/10.1109/ccdc.2018.8407902)
    -   one way to fuse sparse depth sensor data with dense (but
        unscaled) depth estimation.
-   \(2018\) [StereoNet: Guided Hierarchical Refinement forReal-Time
    Edge-Aware Depth
    Prediction](http://openaccess.thecvf.com/content_ECCV_2018/papers/Sameh_Khamis_StereoNet_Guided_Hierarchical_ECCV_2018_paper.pdf)

## RGB-D data and its usage

-   \(2017\) [Depth sensors are the key to unlocking next level computer
    vision
    applications.](https://blog.cometlabs.io/depth-sensors-are-the-key-to-unlocking-next-level-computer-vision-applications-3499533d3246)
    -- introduction to depth sensing methods
-   \(2018\) [RGB-D and deep
    learning](https://bair.berkeley.edu/blog/2018/10/23/depth-sensing/)

## 6D pose estimation

-   \(2017\) [Real-Time Seamless Single Shot 6D Object Pose Prediction
    (MSF)](https://arxiv.org/abs/1711.08848)
    -   problem is from 2D RGB image, infer a 3D box on the object.
        (coordinate still on 2D?)
    -   real-time (50 fps on Titan X), use YOLO-like architecture, then
        apply PnP algorithm
-   \(2018\) (Data related) [Annotation-Free and One-Shot Learning for
    Instance Segmentation of Homogeneous Object
    Clusters](https://arxiv.org/pdf/1802.00383.pdf)
-   \(2018\) [Deep Directional Statistics:Pose Estimation
    withUncertainty
    Quantification](http://openaccess.thecvf.com/content_ECCV_2018/papers/Sergey_Prokudin_Deep_Directional_Statistics_ECCV_2018_paper.pdf)
    -   pose orientation estimation with directional statistics (von
        mises distributions)
-   \(2018\) [Deep Object Pose Estimation for Semantic Robotic Grasping
    of Household Objects (Nvidia)](https://arxiv.org/abs/1809.10790)
    -   use synthetic generated data, better accuracy than previous
        methods
    -   architecture inspired by Convolutional pose machines (similar to
        openpose)
-   \(2018\) [Making Deep Heatmaps Robust to Partial Occlusions for 3D
    Object Pose Estimation](https://arxiv.org/abs/1804.03959)
    -   we want to predict heatmaps of each point in a GT 3D bounding
        box
    -   instead of using full image as an input, we sample small
        patches, then predict full-size heatmaps. we aggregate all the
        output heatmaps then choose the peak in heatmap as predicted
        points.
    -   this way it learns to \"infer\" the point position out of frame,
        using only partial object image patches. hopefully reducing the
        occlusion problem.
-   \(2019\) [Bottom-up Object Detection by Grouping Extreme and Center
    Points](https://arxiv.org/abs/1901.08043)
    -   use heatmaps to predict 5 extreme points (TL,TR,BL,BR, and
        center)
    -   then enumerating all the pairings and calculate the
        \"centeredness\" score --\> higher means better pairings of
        those points.
    -   the heatmap network architecture is \"hourglass\" network.
    -   **pros:** seems robust, get more granualr mask of object shapes
    -   **cons:** maybe speed?

## Others

-   \(2017\) [Real-valued (Medical) Time Series Generation with
    Recurrent Conditional GANs](https://arxiv.org/abs/1706.02633v2)
-   \(2018\) [Anomaly detection with Wasserstein
    GAN](https://arxiv.org/abs/1812.02463v2)
-   \(2019\) [Model-based Deep Reinforcement Learning for Dynamic
    Portfolio Optimization](https://arxiv.org/abs/1901.08740)

## Grasping

### Dataset

-   \(2016\) [ACRV Picking Benchmark
    (APB)](https://arxiv.org/abs/1609.05258v2)
-   \(2015\) [YCB Object Set](https://arxiv.org/abs/1502.03143)
-   GGCNN paper proposes a set of 20 reproducible items for testing,
    com-prising comprising 8 3D printed adversarial objects from Dex-Net
    paper and 12 items from the APB and YCB object sets, which provide a
    wide enough range of sizes, shapes and difficulties to effectively
    compare results while not excluding use by any common robots,
    grippers or camera
-   \(2013\) [Cornell grasping
    dataset](http://pr.cs.cornell.edu/deepgrasping/) - 1k RGBD with
    grasp bbox labels

### Papers

-   \(2017\) [Dex-Net 2.0: Deep Learning to Plan Robust Grasps with
    Synthetic Point Clouds and Analytic Grasp
    Metrics](https://arxiv.org/abs/1703.09312)
-   \(2018\) [Closing the Loop for Robotic Grasping: A Real-time,
    Generative Grasp Synthesis Approach
    (GGCNN)](https://arxiv.org/abs/1804.05172)
    -   a 6-layer segmentation CNN to do real-time closed loop grasping
        (20 ms or 50 hz using desktop GPU)
    -   input: 300x300 inpainted pixel depthmap
    -   output: a **g** vector comprises of
        -   heatmap of grasp quality **Q** \[0,1\]
        -   heatmap of grasp width **W** \[0,150\]
        -   heatmap of grasp angle **phi** \[-pi/2, +pi/2\]

## Body pose estimation

### Dataset

[big list of both body and hand
dataset](http://liris.cnrs.fr/voir/wiki/doku.php?id=datasets)

-   \(2017\) [Posetrack benchmark Dataset](https://posetrack.net/)
    -   20K RGB images (from 500 videos) with 120K body pose labeled
    -   main purpose for the [ICCV 2017 human pose
        challenge](https://posetrack.net/workshops/iccv2017/#people)
        evaluation
-   \(2016\) [COCO keypoint
    challenge](http://cocodataset.org/#keypoints-challenge2016) -
    **good**
    -   90K RGB images
    -   2016 winner is the openpose paper below

### Papers

-   \(2016\) [Realtime Multi-Person 2D Pose Estimation using Part
    Affinity Fields](https://arxiv.org/abs/1611.08050) - **openpose
    paper**
    -   state-of-the-art accuracy and speed
-   \(2017\) [VNect: Real-time 3D Human Pose Estimation with a Single
    RGB Camera](http://gvv.mpi-inf.mpg.de/projects/VNect/)
    -   single-person, real-time **3D** body pose estimation.
    -   RGB data \>\> crop single-person (tracked) \>\> CNN pose
        regression \>\> Kinematic skeleton fitting
    -   So far they only shown a full-body result. Upper-half images
        only might be a problem (kinematic)
    -   not sure about performance.

`=================================================================`{.verbatim}

## Hand pose estimation

The most challenging part about this is not the architecture, but the
lack of large, clean, public dataset.

### Dataset

-   \(2017\) [BigHand2.2M
    Dataset](http://www.iis.ee.ic.ac.uk/ComputerVision/hand/Hands2016)
    -   2.2 million Depth and (maybe) RGB images
    -   no public link.
-   \(2017\) [First-Person Hand Action
    Dataset](https://arxiv.org/abs/1704.02463)
    -   100K RGB+D images
    -   no public link
    -   First-person camera only (like selfies)
-   \(2017\) [Hands Challenge 2017
    Dataset](http://icvl.ee.ic.ac.uk/hands17/challenge/)
    -   sampled from both of the above two dataset
    -   main purpose is for evaluation in the 2017 competition
    -   dataset available via email request, non-commercial purpose only
-   \(2017\) [Multiview 3D Hand Pose
    Dataset](http://www.rovit.ua.es/dataset/mhpdataset/) - **so-so** \|
    **real** \| **ground-truth not accurate**
    -   20K RGB images with 2D,3D, bounding box annotation
-   \(2017\) [Synthetic dataset from Zimmerman
    et.al](https://lmb.informatik.uni-freiburg.de/resources/datasets/RenderedHandposeDataset.en.html) -
    **good** \| **CG**
    -   41K RGB+D images from 20 different characters 3D models (with 1K
        random background).
    -   Basically Zimmerman generated this dataset for \[his own
        architecture\]\[<https://arxiv.org/abs/1705.01389>) use
-   \(2016\) [Capturing Hands in Action using Discriminative Salient
    Points](http://files.is.tue.mpg.de/dtzionas/Hand-Object-Capture/)
    **good** \| **real**
    -   pretty good label for Hand-Hand Interaction. (RGB-D)
-   \(2014\) [RWTH-PHOENIX-Weather MS
    Handshapes](https://www-i6.informatik.rwth-aachen.de/~koller/1miohands-data/) -
    **potential** \| **real** \| **no keypoints**
    -   1 million RGB sign-language hand images with classification
        label.
    -   only has \"shape\" level classification label. Also the cropping
        might not be close enough
-   \(2013\) [polish sign language
    database](http://sun.aei.polsl.pl/~mkawulok/gestures/) - **good** \|
    **real**
    -   1,500 annotated RGB dataset
-   \(2013\) [Dexter 1
    dataset](http://handtracker.mpi-inf.mpg.de/projects/handtracker_iccv2013/dexter1.htm)
    -   3K RGB+D images
    -   only 6 joints
-   \(2014\) [NYU hand pose
    Dataset](http://cims.nyu.edu/~tompson/NYU_Hand_Pose_Dataset.htm#overview)
    -   80K RGB+D images (mostly from a single person)
    -   generally used for paper evaluation
    -   Not good RGB images according to Zimmerman paper

list of more datasets here

-   [Hand, Hand Grasp, Hand Action and Gesture
    Databases](http://homepages.inf.ed.ac.uk/rbf/CVonline/Imagedbase.htm#gesture)
-   [big list of both body and hand
    dataset](http://liris.cnrs.fr/voir/wiki/doku.php?id=datasets)

### Hand Papers

Most of the papers use Depth-only or RGB+D data to estimate hand-pose...
It is probably possible to convert RGB to depth with another model, but
it might be even slower.

-   List of generally good papers with performance benchmark here --\>
    [Awesome hand pose
    estimation](https://github.com/xinghaochen/awesome-hand-pose-estimation)

-   List of papers with notes from researcher student\'s personal wiki
    --\> [inria
    wiki](https://github.com/hassony2/inria-research-wiki/wiki/hand-papers)

-   [Accepted papers from Hands 2017
    conference](http://icvl.ee.ic.ac.uk/hands17/program/program-details/)

-   \(2017\) [Hand Keypoint Detection in Single Images using Multiview
    Bootstrapping](https://arxiv.org/abs/1704.07809) - **openpose**

    -   good accuracy but speed is quite slow. the paper says it can be
        run in real-time but never provide benchmark any.
    -   2D hand pose estimation from RGB image
    -   starts from building multiview dataset with good labels
        -   ****important**** - crop each hand images using body pose to
            estimate area
        -   train a detector to predict joint location on each images
        -   average & contrain in 3D space from multiple view (but same
            hand instance)
        -   get 3D point labels (use as ground truth for next
            interations)
        -   continue until all the images are properly labeled
    -   Detector Architecture: based on
        [CPM](https://arxiv.org/pdf/1602.00134.pdf) with some
        modifications
        -   Stage 1:
            -   Pass input images into a few CNN+Pooling layers to
                extract feature-maps.
            -   pass through a few more CNN layers to predict belief
                maps
        -   Stage 2:
            -   Again, pass input images into a few CNN+Pooling layers
                to extract feature-maps. **These layers have different
                weights from Stage 1**
            -   concatenate with belief maps from Stage 1
            -   use that to pass through a few more CNN layers to
                predict a more refined belief maps
        -   Stage 3 and onward: Use stage 2 architecture and repeat.

-   \(2017\) [Learning to Estimate 3D Hand Pose from Single RGB
    Images](https://arxiv.org/abs/1705.01389)

    -   This is the Zimmerman paper
    -   3 Networks are used sequentially
        -   hand localization through segmentation
        -   21 keypoint (2D) localization in hand
        -   deduction of 3D hand pose from 2D keypoints

-   \(2017\) [SubUNets: End-to-end Hand Shape and Continuous Sign
    Language
    Recognition](http://epubs.surrey.ac.uk/841837/1/camgoz2017iccv.pdf)

    -   architecture: CNN+LSTM+Seq2seq (CTC) \>\> classification
    -   the CTC part is used for doing continuous prediction
    -   [<https://www-i6.informatik.rwth-aachen.de/~koller/>](https://www-i6.informatik.rwth-aachen.de/~koller/)
    -   WITH 1 million hand sign-language dataset (per above)

-   \(2015\) [A novel finger and hand pose estimation technique for
    real-time hand gesture
    recognition](https://sci-hub.io/http://www.sciencedirect.com/science/article/pii/S0031320315002745) -
    **potential**

    -   several ways to represent the hand model, with varying
        complexities -- good way to think about feature representation
    -   This is not a deep learning paper, but there are several
        techniques for pre-processing the RGB images to make them easier
        for the architecture to learn hand pose.

## Anomaly Detection (Images / Videos)

-   Overview
    -   currently there are 3 main approaches
        1.  clustering or nearest neighbor
        2.  learn from 1-class (normal) data and draw a boundary using
            SVM etc.
        3.  feature reconstruction of what is considered \"normal\" and
            compared diff against the sample.
    -   recently DL methods focus on the 3rd approach using autoencoders
        and GANs
-   [Awesome list of anomaly
    detection](https://github.com/hoya012/awesome-anomaly-detection)
-   \(2017\) [Unsupervised Anomaly Detection with Generative Adversarial
    Networks to Guide Marker Discovery (AnoGAN),
    Schlegl.](https://arxiv.org/abs/1703.05921) /
    [code](https://github.com/tkwoo/anogan-keras)
    -   train normal GAN setup to get D and G (in this case they use
        DCGAN)
    -   now get new (potential anomaly) image called \`x\`
    -   back-optimize the input \`z\` of G, using \`x\`
    -   we then use 2 kind of losses to measure anomaly score
        -   residual loss RL(x) = sum(abs(x - G(z)))
        -   feature discrimination loss DL(X) = sum(abs(D~f~(x) -
            D~f~(G(z)))
            -   where D~f~ is a function to get mid-level features from
                D
        -   total~loss~ A(x) = lambda \* DL(x) + (1 - lambda) \* RL(x)
            where they found lamda = 0.1 works best
-   \(2018\) [Efficient GAN-Based Anomaly Detection,
    Zenati](https://arxiv.org/abs/1802.06222) /
    [open-review](https://openreview.net/forum?id=BkXADmJDM) /
    [code](https://github.com/houssamzenati/Efficient-GAN-Anomaly-Detection)
    -   From AnoGAN, replacing DCGAN with BiGAN, so that we can have
        (E)ncoder as inverse mapping from x to z
    -   they use the following score function to detect anomalies
        -   total score A(x) = alpha\*LG(x) + (1 - alpha)\*LD(x)
        -   reconstruction loss LG(x) = abs( x - G(E(x)) )
        -   Discriminator loss LD(x) can be defined in two ways
            -   cross-entropy (CE): between D(x,E(x)) and 1
            -   feature-matching (FM): L0 loss (absolute-diff) between
                mid-level logits of D(x,E(x)) and D(G(E(x)),E(x))
            -   experiments show that performance between CE and FM is
                data-specific
-   \(2018\) [Adversarially Learned Anomaly Detection
    (ALAD)](https://arxiv.org/abs/1812.02288) /
    [code](https://github.com/houssamzenati/Adversarially-Learned-Anomaly-Detection)
    -   This is the follow-up work from the Efficient Anogan paper
        author
    -   they added Spectral Normalization and additional Discriminators
        to get higher accuracy. (All reasonable ideas, however the
        improvement isn\'t that clear-cut, looking at the ablation
        study)
    -   Dataset Tested: KDD, Arrhythmia, CIFAR10, SVHN
-   \(2019\) \[ICLR\'19\] [Do Deep Generative Models Know What They
    Don\'t Know?](https://openreview.net/forum?id=H1xwNhCcYm)
-   \(2018\) [Generative Ensembles for Robust Anomaly
    Detection](https://arxiv.org/abs/1810.01392)
-   \(2018\) [An overview of deep learning based methods for
    unsupervised and semi-supervised anomaly detection in videos,
    Kiran](https://arxiv.org/abs/1801.03149)
    -   this applies specifically to anomaly detection in videos, with
        these datasets:
        -   UCSD Dataset: pedestrians (normal) vs cyclist/wheelchairs
            (abn) etc.
        -   CUHK Avenue Dataset: unusual object or behaviors in Subway
        -   UMN Dataset: unusual crowd activity
        -   Train Dataset: unusual movement of people on trains
        -   London U-turn dataset: normal traffic vs
            jaywalking/firetruck
    -   Methods categorized as following
        -   Representation learning: PCA, Autoencoders (AEs) --\>
            monitor deviation
        -   Predictive modeling: autoregressive models, LSTMs --\>
            predict next frame distributions
        -   Generative model: VAEs, GANs, adversarial AEs (AAEs) --\>
            likelihood
        -   evalutaion:
            -   there are two input options: raw images or optical flow.
                Flow works much better across the board
            -   no model came out consistently on top, and PCA with flow
                did surprisingly well.
-   \(2017\) [Enhancing The Reliability of Out-of-distribution Image
    Detection in Neural Networks,
    Liang](https://arxiv.org/abs/1706.02690) /
    [open-review](https://openreview.net/forum?id=H1VGkIxRZ)
    -   train a DNN model with class of in-distribution data = 1 and
        others = 0. (I think at training time, the target is always 1)
    -   at test time, two transformations are proposed for better
        detection
        -   temperature scaling (T) of softmax probabilities (per
            Hinton\'s [distillation
            paper](https://arxiv.org/abs/1503.02531). `T` is within
            range \[1,1000\]
        -   small perturbations by a gradient of its own raw image\'s
            softmax-score. the scaling factor is in \[0,0.004\]
    -   two key insights:
        -   `Temperature scaling` makes the network less sure and expand
            the outlier area (90-100% prob. part)
        -   `Perturbations` mainly affects in-distribution data, almost
            has no effect for out-distribution data
-   \(2018\) \[NIPS\'18\] [Deep Anomaly Detection Using Geometric
    Transformations](https://nips.cc/Conferences/2018/Schedule?showEvent=11927)
    -   using target as \"transformation #i\" for the labels while
        training
    -   for simple normality score, take the softmaxed prediction for
        each Transformation, then compute mean. The higher, the more
        likely to be normal image.
    -   for full dirichlet normality score, we need to estimate alpha
        first and the formula is a bit more complex.
    -   intuition is that:
        -   while training (which are all normal images), the model will
            learn to detect types of geometric transformation.
        -   on testing, if we have abnormal images, the model will be
            less sure of the type of transformation used.
-   \(2018\) \[NIPS\'18\] [A loss framework for calibrated anomaly
    detection](https://papers.nips.cc/paper/7422-a-loss-framework-for-calibrated-anomaly-detection)
-   \(2018\) [GANomaly: Semi-Supervised Anomaly Detection via
    Adversarial Training](https://arxiv.org/abs/1805.06725)
-   \(2018\) [Improving Unsupervised Defect Segmentation by Applying
    Structural Similarity to
    Autoencoders](https://arxiv.org/abs/1807.02011)
    -   for reconstruction-type anomaly segmentation, using SSIM instead
        of L2 Loss improved the quality substantially.
    -   these guys are from Machine vision company, so this idea is
        probably in actual production.

## Anomaly Detection (Time Series)

-   Overview
    -   3 main approaches
        -   classification - input sequence window ==\> output Good /
            Bad
        -   detection - input sequence window ==\> output t+1 sequence
            and compare diff with DTW
        -   reconstruction - input squence window ==\> Encoder-Decoder
            ==\> check reconstruction loss
-   \(2018\) [Deep learning for time series classification: a
    review](https://arxiv.org/abs/1809.04356)
-   \(2018\) [Anomaly Detection in Multivariate Non-stationary Time
    Series for Automatic DBMS
    Diagnosis](https://arxiv.org/abs/1708.02635)

## Generative Adversarial Networks (GANs)

-   \(2018\) (Articles) [GAN Series (from the beginning to the
    end)](https://medium.com/@jonathan_hui/gan-gan-series-2d279f906e7b)
-   \(2014\) [Generative adversarial nets, I. Goodfellow et
    al.](http://papers.nips.cc/paper/5423-generative-adversarial-nets.pdf)
    -   Objective is to get distribution of generated sample (P~g~) to
        be as close to distribution of real data (P~y~) as much as
        possible
    -   using a minimax game of fight between discriminator (D) and
        generator (G)
    -   the learning process is like this: uniform z --\> G(z) --\>
        D(G(z))
    -   we switch between D(x) and D(G(z)) to learn D
    -   the loss is like this: C(D,G) = minimize log(D(x)) + log(1 -
        D(G(z)))
        -   this is equivalent to C(D,G) = -log(4) + 2\*JS(P~x~ \|\|
            P~g~)
            -   JS is Jensen-Shannon Divergence
        -   a little trick for G to get sizable gradients, the loss used
            is instead: maximize D(G(z))
    -   note that the theory calls for optimizing P~g~ but in practive
        we approximate with function G. the better or more powerful G,
        the closer to P~g~
-   \(2016\) [Adversarial Feature Learning (BiGAN),
    Donahue](https://arxiv.org/abs/1605.09782)
    -   add an Encoder to do inverse mapping. the setup is like this:
        -   (G)enerator: G(z) approximates \`x\`
        -   (E)ncoder: E(x) approximates the latent space vector \`z\`
            (200D of \[-1,1\])
        -   (D)iscriminator: recieves input tuple of either z,G(z) or
            E(x),x then output a probability of input being real
    -   this papers show proof that if we have a perfect Discriminator,
        the G and E must be an inverse mapping of each other
    -   they tried with MNIST, works quite well. Then failed with
        Imagenet -- the model fails to generate realistic looking
        images, although comparing x and G(E(x)) shows some superficial
        consistency, like same structure or color etc.
    -   need to read more about comparison of BiGAN with Autoencoders.
-   \(2016\) [Improved techniques for training GANs, T. Salimans et
    al.](http://papers.nips.cc/paper/6125-improved-techniques-for-training-gans.pdf)

## Style Transfers

-   \(2017\) [Deep Photo Style Transfer, F. Luan et
    al.](http://arxiv.org/pdf/1703.07511v1.pdf)
-   \(2018\) [A Style-Based Generator Architecture for Generative
    Adversarial Networks, Karras et
    al.](https://arxiv.org/abs/1812.04948)

## Understanding / Generalization / Transfer

-   \(2014\) [How transferable are features in deep neural
    networks?](http://papers.nips.cc/paper/5347-how-transferable-are-features-in-deep-neural-networks.pdf)

    -   keypoints
        -   through empirical evidence, researchers notice that for all
            CNN models, the first 1-3 layers are similar
        -   the higher layers (after three) are more specific to the
            classification task
        -   we want to test how \"general\" or \"specific\" for each
            layer
        -   train a real-image classification CNN (7 layers) model-A and
            model-B, using completely seperate classes
        -   freeze 3 lowest layers from model A, then put the 4 higher
            layer with random weight, then train with model B dataset
        -   the resulting accuracy does not change
        -   and actually if we don\'t freeze (let it fine-tune), the
            accuracy is higher (it generalizes better)

-   \(2014\) [CNN features off-the-Shelf: An astounding baseline for
    recognition](http://www.cv-foundation.org//openaccess/content_cvpr_workshops_2014/W15/papers/Razavian_CNN_Features_Off-the-Shelf_2014_CVPR_paper.pdf)

    -   keypoints

        -   comparison of state-of-the-art \"manual\" feature
            engineering (SIFT etc.) vs \"OVERFEAT\" CNN
        -   Summary from the paper:

        It's all about the features! SIFT and HOG descriptors produced
        big performance gains a decade ago and now deep convolutional
        features are providing a similar breakthroughfor recognition.

        Thus, applying the well-established com-puter vision procedures
        on CNN representations should potentially push the reported
        results even further. In any case,if you develop any new
        algorithm for a recognition task thenitmustbe compared against
        the strong baseline ofgenericdeep features+simple classifier.

-   \(2014\) [Learning and transferring mid-Level image representations
    using convolutional neural
    networks](http://www.cv-foundation.org/openaccess/content_cvpr_2014/papers/Oquab_Learning_and_Transferring_2014_CVPR_paper.pdf)

    -   keypoints
        -   same idea as the \"transferable features in DNN\" paper
        -   use the pre-trained weights from task A (ImageNet) to apply
            to task B (Pascal)
        -   they transferred all the weights (all CNN and FCs layers),
            froze them , and added 2 FC layers at the end to adapt to
            new output
        -   for task B (Pascal), the pictures are cropped to specific
            object, so they use a sliding window to generate new pics +
            \"background\" class

-   \(2014\) [Visualizing and understanding convolutional
    networks](http://arxiv.org/pdf/1311.2901)

    -   keypoints
        -   Building from 2011 papers, they use deconvnet to analyze the
            CNN layers.

-   \(2014\) [Decaf: A deep convolutional activation feature for generic
    visual recognition, J. Donahue et
    al.](http://arxiv.org/pdf/1310.1531)

-   \(2015\) [Distilling the knowledge in a neural
    network](http://arxiv.org/pdf/1503.02531)

    -   keypoints
        -   train the complex model first (model-A)
        -   then train a simpler one using loss function that combines
            (same dataset) and (model-A prediction)
        -   divide by certain constant (lambda) to change how sensitive
            the difference for each classes is

-   \(2015\) [Deep neural networks are easily fooled: High confidence
    predictions for unrecognizable
    images](http://arxiv.org/pdf/1412.1897)

    -   keypoints
        -   use the CNN model\'s prediction probabilities as input
        -   use an evolution algorithm to evolve a random image to fool
            the model
        -   some images are similar to the \"real\" thing, some looks
            just like static TV noise
        -   using the \"static\" images to retrain, still difficult to
            patch up the weakness
        -   is this similar to adversarial network?

## Optimization / Training Techniques

-   \(2012\) [Random search for hyper-parameter
    optimization](http://www.jmlr.org/papers/volume13/bergstra12a/bergstra12a)

-   \(2015\) [Batch normalization: Accelerating deep network training by
    reducing internal covariate shift, S. Loffe and C.
    Szegedy](http://arxiv.org/pdf/1502.03167)

-   \(2015\) [Delving deep into rectifiers: Surpassing human-level
    performance on imagenet classification, K. He et
    al.](http://www.cv-foundation.org/openaccess/content_iccv_2015/papers/He_Delving_Deep_into_ICCV_2015_paper.pdf)

-   \(2014\) [Dropout: A simple way to prevent neural networks from
    overfitting, N. Srivastava et
    al.](http://jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf)

-   \(2014\) [Adam: A method for stochastic optimization, D. Kingma and
    J.Ba](http://arxiv.org/pdf/1412.6980)

-   \(2012\) [Improving neural networks by preventing co-adaptation of
    feature detectors, G. Hinton et
    al.](http://arxiv.org/pdf/1207.0580.pdf)

-   \(2017\) [A summary of gradient descent optimization
    algorithms](http://ruder.io/optimizing-gradient-descent/index.html#gradientdescentoptimizationalgorithms)

    -   keypoints
        -   **TLDR; - Use Adam, then try others if it doesn\'t work**
        -   SGD - basic gradient descent
        -   mini-batch - update once every batch
        -   online - update once every sample
        -   momentum - running faster and faster into the general
            direction of local minima
        -   Nesterov - to prevent overshooting cause by momentum, we can
            \"correct\" it by first calculate momentum, then add the
            loss of current param diff with the momentum.
        -   Adagrad - it has a unique learning rate for each
            parameter i. The learning rate is normalized based on past
            gradient values of that parameters. Weakness is that it
            makes learning rates go infinitely small.
        -   Adadelta - fix the learning rate shrinking problem. by
            replacing the scaling term with RMSE.
        -   RMSprop - similar to Adadelta, developed by Hinton during
            class.
        -   Adam - has first and second moments of gradients.
            essentially Momentum + RMSprop
        -   AdaMax - generalized Adam to n moments
        -   Nadam - Nesterov + Adam

## Unsupervised / Generative Models

-   \(2013\) [Auto-encoding variational Bayes, D. Kingma and M.
    Welling](http://arxiv.org/pdf/1312.6114)
-   \(2013\) [Building high-level features using large scale
    unsupervised learning, Q. Le et al.](http://arxiv.org/pdf/1112.6209)
-   \(2015\) [Unsupervised representation learning with deep
    convolutional generative adversarial networks, A. Radford et
    al.](https://arxiv.org/pdf/1511.06434v2)
-   \(2015\) [DRAW: A recurrent neural network for image generation,
    K.Gregor et al.](http://arxiv.org/pdf/1502.04623)
-   \(2016\) [Pixel recurrent neural networks (PixelRNN), A. Oord et
    al.](http://arxiv.org/pdf/1601.06759v2.pdf)

## CNN Feature Extractors

-   Backbone feature extractor short summary /
    [source](https://arxiv.org/pdf/1804.06215.pdf)
    -   The backbone network for object detection are usually borrowed
        from the ImageNet classification.
    -   Many new networks are designed to get higher performance for
        ImageNet. AlexNet (2012) is among the first to try to increase
        the depth of CNN. In order to reduce the network computation and
        increase the valid receptive field, AlexNet down-samples the
        feature map with 32 strides which is a standard setting for the
        following works. It also implemented group convolutions (branch
        into two CNN tracks to train on seperate GPU simutaneously) but
        mostly because of engineering constraint (3GB VRAM limit)
    -   VGGNet (2014) stacks 3x3 convolution operation to build a deeper
        network, while still involves 32 strides in feature maps. Most
        of the following researches adopt VGG like structure, and design
        a better component in each stage (split by stride).
    -   GoogleNet (2015) proposes a novel inception block to involve
        more diversity features.
    -   ResNet (2015) adopts "bottleneck" design with residual sum
        operation in each stage, which has been proved a simple and
        efficient way to build a deeper neural network.
    -   ResNext (2016) and Xception (2016) use group convolution layer
        to replace the traditional convolution. It reduces the
        parameters and increases the accuracy simultaneously.
    -   DenseNet densely concat several layers, it further reduces
        parameters while keeping competitive accuracy. Another different
        research is Dilated Residual Network which extracts features
        with less strides. DRN achieves notable results on segmentation,
        while has little discussion on object detection. There are still
        lots of research for efficient backbone, such as \[17,15,16\].
        However they are usually designed for classification.
-   \(2012\) [(AlexNet) ImageNet classification with deep convolutional
    neural networks, A. Krizhevsky et
    al.](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)
-   \(2013\) [OverFeat: Integrated recognition, localization and
    detection using convolutional networks, P. Sermanet et
    al.](http://arxiv.org/pdf/1312.6229)
-   \(2013\) [Maxout networks, I. Goodfellow et
    al.](http://arxiv.org/pdf/1302.4389v4)
-   \(2013\) [Network in network, M. Lin et
    al.](http://arxiv.org/pdf/1312.4400)
-   \(2014\) [Very deep convolutional networks for large-scale image
    recognition, K. Simonyan and A.
    Zisserman](http://arxiv.org/pdf/1409.1556)
-   \(2014\) [Spatial pyramid pooling in deep convolutional networks for
    visual recognition, K. He et al.](http://arxiv.org/pdf/1406.4729)
-   \(2014\) [Return of the devil in the details: delving deep into
    convolutional nets, K. Chatfield et
    al.](http://arxiv.org/pdf/1405.3531)
-   \(2015\) [Spatial transformer network, M. Jaderberg et
    al.](http://papers.nips.cc/paper/5854-spatial-transformer-networks.pdf)
-   \(2015\) [Going deeper with convolutions, C. Szegedy et
    al.](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Szegedy_Going_Deeper_With_2015_CVPR_paper.pdf)
-   \(2016\) [Rethinking the inception architecture for computer
    vision,C. Szegedy et
    al.](http://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Szegedy_Rethinking_the_Inception_CVPR_2016_paper.pdf)
-   \(2016\) [Inception-v4, inception-resnet and the impact of residual
    connections on learning, C. Szegedy et
    al.](http://arxiv.org/pdf/1602.07261)
-   \(2016\) [Identity Mappings in Deep Residual Networks, K. He et
    al.](https://arxiv.org/pdf/1603.05027v2.pdf)
-   \(2016\) [Deep residual learning for image recognition, K. He et
    al.](http://arxiv.org/pdf/1512.03385)

## Image: Object Detection

-   \(2020\) [Object Detection and Tracking in
    2020](https://blog.netcetera.com/object-detection-and-tracking-in-2020-f10fb6ff9af3)
    (medium article)
-   \(2020\) [IterDet: Iterative Scheme for ObjectDetection in Crowded
    Environments](https://arxiv.org/abs/2005.05708v1)
    -   could be useful for edge device, simialr to gif img loading.
-   (2018-09) [recent advances in object detection in the age of deep
    CNNs](https://arxiv.org/pdf/1809.03193.pdf)
    -   YOLO family
        -   YOLOv1
            -   simple network design, one-shot detector
            -   result (voc 07-12) - mAP(0.5) 63.4 with 45 FPS at
                554x554 on Titan X
        -   YOLOv2
            -   add batch normalization, able to train deeper network
            -   double input resolution 224x224 --\> 448x448 (also in
                Imagenet pretraining)
            -   add anchor box priors, will custom clustering to find
                best priors
            -   result (voc 07-12) - mAP(0.5) 78.6 with 40 FPS at
                554x554 on Titan X
        -   YOLOv3
            -   predict boxes at 3 different scales (similar to SSD)
            -   use skip connection (upsampled then concat layers)
            -   much deeper feature extractors (Darknet-53)
            -   result (COCO) - mAP(0.5) 57.9 with 20 FPS at 608x608 on
                Titan X
    -   [R-CNN
        family](http://cs231n.stanford.edu/slides/2018/cs231n_2018_ds06.pdf)
        -   R-CNN: Selective search → Cropped Image → CNN
        -   Fast R-CNN: Selective search → Crop feature map of CNN
        -   Faster R-CNN: CNN → Region-Proposal Network → Crop feature
            map of CN\*\*
        -   Best accuracy but slow

## Image: Segmentation

-   \(2015\) [Fully convolutional networks for semantic
    segmentation](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Long_Fully_Convolutional_Networks_2015_CVPR_paper.pdf)

    -   keypoints
        -   demonstrate an fully CNN without FC layers at the end --
            without additional manual manipulation

-   \(2014\) [Rich feature hierarchies for accurate object detection and
    semantic segmentation, R. Girshick et
    al.](http://www.cv-foundation.org/openaccess/content_cvpr_2014/papers/Girshick_Rich_Feature_Hierarchies_2014_CVPR_paper.pdf)

-   \(2015\) [Semantic image segmentation with deep convolutional nets
    and fully connected CRFs, L. Chen et
    al.](https://arxiv.org/pdf/1412.7062)

-   \(2013\) [Learning hierarchical features for scene labeling, C.
    Farabet et
    al.](https://hal-enpc.archives-ouvertes.fr/docs/00/74/20/77/PDF/farabet-pami-13.pdf)

## Image / Video / Etc

-   \(2016\) [Image Super-Resolution Using Deep Convolutional
    Networks, C. Dong et al.](https://arxiv.org/pdf/1501.00092v3.pdf)
-   \(2015\) [A neural algorithm of artistic style, L. Gatys et
    al.](https://arxiv.org/pdf/1508.06576)
-   \(2015\) [Deep visual-semantic alignments for generating image
    descriptions, A. Karpathy and L.
    Fei-Fei](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Karpathy_Deep_Visual-Semantic_Alignments_2015_CVPR_paper.pdf)
-   \(2015\) [Show, attend and tell: Neural image caption generation
    with visual attention, K. Xu et
    al.](http://arxiv.org/pdf/1502.03044)
-   \(2015\) [Show and tell: A neural image caption generator, O.
    Vinyals et
    al.](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Vinyals_Show_and_Tell_2015_CVPR_paper.pdf)
-   \(2015\) [Long-term recurrent convolutional networks for visual
    recognition and description, J. Donahue et
    al.](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Donahue_Long-Term_Recurrent_Convolutional_2015_CVPR_paper.pdf)
-   \(2015\) [VQA: Visual question answering, S. Antol et
    al.](http://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Antol_VQA_Visual_Question_ICCV_2015_paper.pdf)
-   \(2014\) [DeepFace: Closing the gap to human-level performance in
    face verification, Y. Taigman et
    al.](http://www.cv-foundation.org/openaccess/content_cvpr_2014/papers/Taigman_DeepFace_Closing_the_2014_CVPR_paper.pdf):
-   \(2014\) [Large-scale video classification with convolutional neural
    networks, A. Karpathy et
    al.](http://vision.stanford.edu/pdf/karpathy14.pdf)
-   \(2014\) [DeepPose: Human pose estimation via deep neural networks,
    A.Toshev and C.
    Szegedy](http://www.cv-foundation.org/openaccess/content_cvpr_2014/papers/Toshev_DeepPose_Human_Pose_2014_CVPR_paper.pdf)
-   \(2014\) [Two-stream convolutional networks for action recognition
    in videos, K. Simonyan et
    al.](http://papers.nips.cc/paper/5353-two-stream-convolutional-networks-for-action-recognition-in-videos.pdf)
-   \(2013\) [3D convolutional neural networks for human action
    recognition, S. Ji et
    al.](http://machinelearning.wustl.edu/mlpapers/paper_files/icml2010_JiXYY10.pdf)

## Natural Language Processing / RNNs

-   \(2016\) [Neural Architectures for Named Entity Recognition, G.
    Lample et al.](http://aclweb.org/anthology/N/N16/N16-1030.pdf)
-   \(2016\) [Exploring the limits of language modeling, R. Jozefowicz
    et al.](http://arxiv.org/pdf/1602.02410)
-   \(2015\) [Teaching machines to read and comprehend, K. Hermann et
    al.](http://papers.nips.cc/paper/5945-teaching-machines-to-read-and-comprehend.pdf)
-   \(2015\) [Effective approaches to attention-based neural machine
    translation, M. Luong et al.](https://arxiv.org/pdf/1508.04025)
-   \(2015\) [Conditional random fields as recurrent neural networks,
    S.Zheng and S.
    Jayasumana.](http://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Zheng_Conditional_Random_Fields_ICCV_2015_paper.pdf)
-   \(2014\) [Memory networks, J. Weston et
    al.](https://arxiv.org/pdf/1410.3916)
-   \(2014\) [Neural turing machines, A. Graves et
    al.](https://arxiv.org/pdf/1410.5401)
-   \(2014\) [Neural machine translation by jointly learning to align
    and translate, D. Bahdanau et al.](http://arxiv.org/pdf/1409.0473)
-   \(2014\) [Sequence to sequence learning with neural networks, I.
    Sutskever et
    al.](http://papers.nips.cc/paper/5346-sequence-to-sequence-learning-with-neural-networks.pdf)
-   \(2014\) [Learning phrase representations using RNN encoder-decoder
    for statistical machine translation, K. Cho et
    al.](http://arxiv.org/pdf/1406.1078)
-   \(2014\) [A convolutional neural network for modeling sentences, N.
    Kalchbrenner et al.](http://arxiv.org/pdf/1404.2188v1)
-   \(2014\) [Convolutional neural networks for sentence
    classification, Y. Kim](http://arxiv.org/pdf/1408.5882)
-   \(2014\) [Glove: Global vectors for word representation, J.
    Pennington et al.](http://anthology.aclweb.org/D/D14/D14-1162.pdf)
-   \(2014\) [Distributed representations of sentences and documents,
    Q.Le and T. Mikolov](http://arxiv.org/pdf/1405.4053)
-   \(2013\) [Distributed representations of words and phrases and their
    compositionality, T. Mikolov et
    al.](http://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf)
-   \(2013\) [Efficient estimation of word representations in vector
    space, T. Mikolov et al.](http://arxiv.org/pdf/1301.3781)
-   \(2013\) [Recursive deep models for semantic compositionality over a
    sentiment treebank, R. Socher et
    al.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.383.1327&rep=rep1&type=pdf)
-   \(2013\) [Generating sequences with recurrent neural networks, A.
    Graves.](https://arxiv.org/pdf/1308.0850)

## Speech / Other Domain

-   \(2020\) [Gwern\'s May newsletter about GPT-3 language model and its
    history](https://www.gwern.net/newsletter/2020/05#gpt-3)

-   \(2016\) [End-to-end attention-based large vocabulary speech
    recognition, D. Bahdanau et al.](https://arxiv.org/pdf/1508.04395)

-   \(2015\) [Deep speech 2: End-to-end speech recognition in English
    and Mandarin, D. Amodei et al.](https://arxiv.org/pdf/1512.02595)

-   \(2013\) [Speech recognition with deep recurrent neural networks, A.
    Graves](http://arxiv.org/pdf/1303.5778.pdf)

-   \(2012\) [Deep neural networks for acoustic modeling in speech
    recognition: The shared views of four research groups, G. Hinton et
    al.](http://www.cs.toronto.edu/~asamir/papers/SPM_DNN_12.pdf)

-   \(2012\) [Context-dependent pre-trained deep neural networks for
    large-vocabulary speech recognition, G. Dahl et
    al.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.337.7548&rep=rep1&type=pdf)

-   \(2012\) [Acoustic modeling using deep belief networks, A. Mohamed
    et al.](http://www.cs.toronto.edu/~asamir/papers/speechDBN_jrnl.pdf)

-   \(2017\) [CTC (Connectionist Temporal Classification Loss)
    Explained](https://gab41.lab41.org/speech-recognition-you-down-with-ctc-8d3b558943f0)

    -   Keypoints
        -   In normal systems, we cut the audio signal into very small
            slices and feed them to RNN.
        -   The predictions then become something like (for \"CAT\") --
            \"...C..A..AA..A..AA.T..TT..\"
        -   so obviously we need to get rid of the silence and repeats,
            the way to do that is CTC.
        -   Essentially, the equation defines the loss that makes good
            probability distribution over good paths

## Reinforcement Learning / Robotics

-   \(2016\) [End-to-end training of deep visuomotor policies, S. Levine
    et
    al.](http://www.jmlr.org/papers/volume17/15-522/source/15-522.pdf)

-   \(2016\) [Learning Hand-Eye Coordination for Robotic Grasping with
    Deep Learning and Large-Scale Data Collection, S. Levine et
    al.](https://arxiv.org/pdf/1603.02199)

-   \(2016\) [Asynchronous methods for deep reinforcement learning, V.
    Mnih et al.](http://www.jmlr.org/proceedings/papers/v48/mniha16.pdf)

-   \(2016\) [Deep Reinforcement Learning with Double Q-Learning, H.
    Hasselt et al.](https://arxiv.org/pdf/1509.06461.pdf)

-   \(2016\) [Mastering the game of Go with deep neural networks and
    tree search, D. Silver et
    al.](http://www.nature.com/nature/journal/v529/n7587/full/nature16961.html)

-   \(2015\) [Continuous control with deep reinforcement learning, T.
    Lillicrap et al.](https://arxiv.org/pdf/1509.02971)

-   \(2015\) [Human-level control through deep reinforcement
    learning, V. Mnih et
    al.](http://www.davidqiu.com:8888/research/nature14236.pdf)

-   \(2015\) [Deep learning for detecting robotic grasps, I. Lenz et
    al.](http://www.cs.cornell.edu/~asaxena/papers/lenz_lee_saxena_deep_learning_grasping_ijrr2014.pdf)

-   \(2012\) [A painless Q-learning
    tutorial](http://mnemstudio.org/path-finding-q-learning-tutorial.htm)

    -   keypoints
        -   Q-learning is a reinforcement learning algorithm. It is
            suitable for problem which has finite number of states and
            we know the value of all state\'s immediate reward.
        -   the main idea is do semi-random exploring to eventually map
            out an expected rewards value of that state. The expected
            value is the sum of current and all future rewards value
            (given discount factors).
        -   So we will have a big rewards matrix (R) where row equals
            current state and column equals an action to next state. The
            values are the rewards when taking that action (and arriving
            at a new state).
        -   We will also have a memory matrix (Q). which contains a sum
            of expected immediate and future rewards. Row is current
            state and column is the next future state.
        -   the update formula is as follows:
            -   Q(state,action) = R(current~state~,action) + Gamma \*
                max\[ Q(immediate~nextstate~,all~actions~) \]
                -   where...
                -   R = reward matrix
                -   Q = memory matrix
                -   Gamma = discount factor
                -   This assumes a learning rate of 1. If we want a
                    different learning rate, we can do:
                    -   Q~new~ = Q~old~ + learning~rate~ \* (Q~update~ -
                        Q~old~)

-   \(2013\) [Playing atari with deep reinforcement
    learning](http://arxiv.org/pdf/1312.5602.pdf)

    -   keypoints
        -   aasdf

-   \(2015\) [David Silver\'s excellent reinforcement learning course
    with
    video](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html)

    -   Agents, Environments, Actions, Rewards
    -   Full information game --\> Agent state = Environment state
    -   History = sequences of Observations, Agent States and Actions.
    -   Markov process means P(St) = P(St \| St+1..), so previous states
        don\'t matter.
    -   partially observable markovs (POMDP)
    -   Policy = function that maps from Agent state to Action
    -   Value function = estimates total future reward given current
        state St

-   \(2017\) [A Brief Survey of Deep Reinforcement
    Learning](https://arxiv.org/pdf/1708.05866)

    -   keypoints
        -   In this survey, we begin withan introduction to the general
            field of reinforcement learning, then progress to the main
            streams of value-based and policy-based methods. Our survey
            will cover central algorithms indeep reinforcement learning,
            including the deep Q-network,trust region policy
            optimisation, and asynchronous advantage actor-critic.
        -   General RL concepts
            -   Reward-Driver Behavior
                -   the essense of RL is interaction. the interaction
                    loop is simple.
                    1.  given current state --\> choose action
                    2.  execute action
                    3.  arrives at new state (received new state data
                        and its rewards)
                    4.  go to 1. until terminal state
                -   Per sequence above, we want to derive \"optimal
                    policy\" so that the agents can asymtotically get
                    \"optimal\" rewards --\> which means a highest
                    expected value of aggregated future rewards with a
                    certain discount factor.
                -   Formally, RL can be described as a Markov decision
                    process (MDP). For (only) partially-observable
                    states like in the real world, there is a
                    generalization of MDP called POMDP.
                -   Challenges in RL: long sequences until reward
                    (credit assignment problem) and temporal sequence
                    correlation
            -   Reinforcement Learning Algorithms
                -   Concept I: estimating Value function (total expected
                    Rewards)
                    -   Dynamic Programming:
                        -   define: V = total expected Rewards (R) ,
                            Q\|s,a is conditional V given state s and
                            action a
                        -   define: Y = R(t) + disc \* Q\|s(t+1),a(t+1)
                        -   define: Temporal difference (TD) error = Y -
                            Q\|s,a
                        -   to get Q\|s,a , we use Q-learning method and
                            try to minimize the TD error
                    -   Concept II: sampling -- random walk till the end
                        to get all Rs
                        -   so instead of going breadth-search like
                            \[I\], we do depth-first
                        -   we can use Monte Carlo (MC) to get multiple
                            returns and average them.
                        -   it is easier to learn that one actions lead
                            to much better consequences than the other
                            (a fork in the road)
                        -   define: relative advantage A = V - Q
                        -   we use an idea of \"advantage update\" in
                            many recent algorithms
                    -   Concept III: policy search
                        -   instead of estimating value function, we try
                            to contruct policy directly. (so we can
                            sample actions from it)
                        -   try several policies to get the optimal one,
                            using either gradient-based or gradient-free
                            optimization.
                        -   Policy Gradients
                            -   get the approximate V diff from
                                different policies
                            -   interate policy parameters to know the
                                diff on each one
                            -   change the params to optimize policy
                            -   there are several ways to estimate the
                                diff -- Finite Diference, Likelihood
                                Ratio etc.
                        -   Actor-Critic Methods
                            -   Use Actor (policy driven) to choose
                                actions and learn feedback from Critic
                                (value function).
                            -   Alphago uses this
                    -   Summary
                        -   Shallow sequence, no branching --\> one-step
                            TD learning
                        -   Shallow sequence, many branching --\>
                            dynamic programming
                        -   Deep sequences, no branching --\>
                            many-steps (MC) TD learning
                        -   Deep sequence, many branching --\>
                            exhaustive search

## Credit card fraud detection

-   \(2014\) Literature Survey

    -   algorithms
        -   HMM
        -   NN
        -   Decision Tree
        -   SVM
        -   Genetic Algorithm
        -   Meta Learning Strategy
        -   Biologicla Immune System

## Weather Classification

-   Overall Summary as of \[2018-10\]

There are no agreed upon public dataset and very few DL papers dedicated
to the topic.

The common dataset used is (2014) sunny/cloudy dataset with 10k images.
Other recent papers (2018) have contructed their own dataset which are
not opened to public yet. However, BDD100K dataset also has weather
attribute labeled, so we should consider using that.

There are 3 type of models proposed thus far.

1.  \(2014\) traditional feature engineering then use SVM/other
    clustering methods.
2.  \(2015\) pure CNN feature extraction then classify
3.  \(2018\) CNN-RNN and/or the combination of DL and traditional
    features.

so far the DL method did out-perform traditional ones.

New alternative would be to add new sensor data (temperature/humidity)
and ensemble with CNN model. For that matter, how accurate would
predictions from sensor data alone be?

-   \(2018\) (2 Dataset) A CNN--RNN architecture for multi-label weather
    recognition (use sci-hub to get the link)

    -   keypoints
        -   recognize that weather classes are not exclusive to each
            other (for example, can be both sunny and foggy) so should
            classify accordingly (not using softmax or binary)
        -   add 2 new datasets (8k - 7 classes) and (10k - 5 classes)
            for multi-labeling comparison
        -   use CNNs as feature extractor
        -   use \"channel-wise attentions\" which is a set of weights to
            amplify/lower each channel\' response.
        -   use \"Convolutional\" LSTM to retain spatial information
            (not flattening to 1-D vectors)
        -   flatten the output \"hidden state\" to predict weather class
        -   then we repeat the step (in LSTM + getting new attention
            weights) to predict next weather class. If there are 5
            classes, the LSTM will run for 5 steps. (This is weird..
            because the problem is not time-based. and this runs from
            single image input)

-   \(2018\) [(Dataset)(Bad) Weather Classification: A new multi-class
    dataset, data augmentation approach and comprehensive evaluations of
    CNNs](https://arxiv.org/abs/1808.00588v1)

    -   keypoints
        -   new dataset (3K) - use 3 classes (rain, fog, snow) with
            equal split
        -   later add sunny/cloudy from past dataset to get 5k (again,
            equal split)
        -   In addition to raw image, they use superpixel (algo to
            cluster pixels together for further processing - google it)
            to ovelay on the image then feed to CNN feature extractors
        -   finally, use some sort of SVMs as binary classifier for each
            class
        -   overall achieved around 80-90% accuracy, with Resnet50 being
            the best extractor overall.
        -   however, no mention of baseline (w/o superpixel) comparison.
            No justification of doing things, even just running their
            model through old sunny/cloudy dataset for comparison. bad
            paper.

-   \(2017\) [(Dataset) (Bad) Transfer Learning for Rain Detection in
    Images](https://repository.tudelft.nl/islandora/object/uuid%3A3bf546c0-a254-4c72-9ee4-02a0919c1624)

    -   keypoints
        -   tried Resnet-18 with various experiments on custom 400k
            rain-no-rain dataset
        -   just bad all around. specific optimization to specific
            dataset. no baseline model. not useful.

-   \(2015\) [Weather Classification with Deep Convolutional
    Network](http://www.academia.edu/18539252/WEATHER_CLASSIFICATION_WITH_DEEP_CONVOLUTIONAL_NEURAL_NETWORKs)

    -   keypoints
        -   use sunny/cloudy 10k dataset
        -   applies AlexNet architecture to this problem
        -   also compared the pretrained with ImageNet AlexNet + SVM vs
            train with weather data from scratch - conclusion is earlier
            base layers are quite general
        -   achieved 91% accuracy (82% normalized)

-   \(2014\) [(Dataset) Two-class Weather Classification (with
    sunny/cloudy 10k
    dataset)](http://www.cse.cuhk.edu.hk/leojia/projects/weatherclassify/index.htm)

    -   keypoints
        -   introduces the 10k weather dataset with 2 classes - sunny
            and cloudy
        -   use traditional computer vision method to classify
            -   custom feature engineering extracting 5 features -- sky,
                shadow, reflection, contrast, haze.
            -   concat all features into 621-D vectors then use complex
                voting schemes to classify based on the existing of
                combinations of features. Tried SVM but didn\'t work
                well.
            -   achieved 76% accuracy (53% normalized)

## Autonomous Driving

-   \[2017-02\] [overview paper](https://www.mdpi.com/2075-1702/5/1/6)

## Face Detection

-   Dataset:
    [WiderFace](http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/)
    -   30K images, 400k faces.
    -   metric is PR curve, split by easy / medium / hard cases
-   \(2004\) [Robust Real-time Object Detection
    (Viola-Jones)](https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/viola-IJCV-01.pdf)
    -   Traditional system with impressive performance

        Input = 384x288 grayscale image, 15 FPS on 700 Mhz Intel Pentium
        III

    -   Algo = Simple Features + Adaboost + Cascade

        1.  Features = sum of two regions and diffs with each other (for
            every pixel coordinate)
        2.  Since there are a lot of features, use Adaboost select a set
            of strongest weak classifiers weak classifer is basically
            this --\> H = if single~feature~ \> threshold then 1 else 0
        3.  Attentional cascade - train a simple 2-feature classifier to
            simply reject no-face image. Then queue up all the
            sub-windows (overlap cropping?), evaluate and reject, then
            use stronger classifier from #2 on the remaining
            sub-windows.
-   \(2014\) [One millisecond face alignment with an ensemble of
    regression trees - Dlib uses this
    ](https://pdfs.semanticscholar.org/d78b/6a5b0dcaa81b1faea5fb0000045a62513567.pdf)
    -   Use cascade of regressor method to detect facial landmarks
        (given that the image is already cropped to face area) claims 1
        ms performance with unknown CPU. has error rate of 0.049 on
        HELEN face dataset. (2,000 training / 500 test image)
    -   Algo = Default positions + features + gradient boosting +
        cascade
        -   we can set up a default landmark (smiley face) in the image
            center or do an average of positions from a big dataset.
        -   then we regress -- computing an update regressors for each
            landmark x,y --\> moving them closer to the face in image.
        -   the features for regressions are diff in pixel intensities,
            the pixel coordinate is relative to the default face shape.
-   \(2017\) [FaceBoxes: A CPU Real-time Face Detector with High
    Accuracy](https://arxiv.org/abs/1708.05234)
    -   custom (light-weight) CNN architecture. No novel idea. (the
        paper has a good summary of past papers however)
        -   runs at 20 FPS on a single CPU core and 125 FPS using a GPU
            for VGA (640x480) images.
    -   some strategy for lightweighted architecture
        -   reduce spatial size of input as quickly as possible
        -   choose suitable kernel size - in their case it\'s 7x7, 5x5,
            3x3
        -   reduce number of output channel
        -   use multi-scale anchor boxes output, but know where to have
            \"dense\" number of predictions.
    -   postprocessing is common pipeline: lots of prediction \>
        thresholding prob \> NMS.
-   \(2017\) [Deep Face Recognition: A
    Survey](https://arxiv.org/abs/1804.06655v1)
    -   Good review of modern face recognition systems. collections of
        recent techniques. It\`s not face detection though.
-   \(2018\) [SFace: An Efficient Network for Face Detection in Large
    Scale Variations (Megvii Inc.
    Face++)](https://arxiv.org/abs/1804.06559v2)
    -   A new dataset called 4K-Face is also introduced to evaluate the
        performance of face detection with extreme large scale
        variations.
        -   The SFace architecture shows promising results on the new
            4K-Face benchmarks.
        -   In addition, our method can run at 50 frames per second
            (fps) with an accuracy of 80% AP on the standard WIDER FACE
            dataset, which outperforms the state-of-art algorithms by
            almost one order of magnitude in speed while achieves
            comparative performance.
-   Benchmark - Labeled Faces in the Wild (LFW) dataset - [state of the
    art
    results](http://vis-www.cs.umass.edu/lfw/results.html#UnrestrictedLb)
    -   most commercial systems get \> 99.0% classification accuracy,
        including Dlib
    -   update as of beginning of 2018

## Own discovery of Research Papers

-   \(2017\) [Mobilenets](https://arxiv.org/pdf/1704.04861.pdf)

-   \(2011\) [Adaptive Deconvolutional Networks for Mid and High Level
    Feature
    Learning](http://www.matthewzeiler.com/pubs/iccv2011/iccv2011.pdf)

    -   keypoints
        -   iterations from the 2010 paper, add unpooling
            reconstrucitons with switches (location info for the
            max-pool values)
        -   they are able to re-create the input-size map for all layers

-   \(2010\) [Deconvolutional
    Networks](http://www.matthewzeiler.com/pubs/cvpr2010/cvpr2010.pdf)

    -   keypoints
        -   Deconvolution is actually \"transposed convolution\"
        -   essentially, it uses feature map to compose back to the
            original images, like legos.
        -   The kernels are different from the feed-forward kernels, of
            course.
        -   the usage of \"sparse coding\" made this possible. see:
            [tranposed convolution
            arithmetic](http://deeplearning.net/software/theano_versions/dev/tutorial/conv_arithmetic.html#transposed-convolution-arithmetic)
        -   [see stackexchange answer from
            here](https://datascience.stackexchange.com/questions/6107/what-are-deconvolutional-layers)
        -   [good slide
            here](http://cs.nyu.edu/~fergus/drafts/utexas2.pdf)

-   \(2016\) [Learning Deep Features for Discriminative Localization
    (global average
    pooling)](http://cnnlocalization.csail.mit.edu/Zhou_Learning_Deep_Features_CVPR_2016_paper.pdf)

    -   keypoints
        -   using \"global average pooling\" method with each featuremap
            on the last layer of CNN.
        -   then we can use the FC weights to combined the GAP values.
        -   this effectively \"focuses\" the network activations before
            connecting to FC layer.
        -   with this we can generate heatmap to see the activation
            overlays

-   \(2015\) [SegNet: A Deep Convolutional Encoder-Decoder Architecture
    for Image Segmentation](https://arxiv.org/pdf/1511.00561.pdf)

    -   this is basically an autodecoder, except for CNN architecture.
        Also use final targets as the segmentation labels.

-   \(2011\) [How Brains Are Built: Principles of Computational
    Neuroscience](https://arxiv.org/pdf/1704.03855.pdf)

    -   precise simulation of the brain chemically is very difficult.
        However, we can possibly create the brain model that is
        \"computationally\" accurate. we can even use this model to
        experiment and fix what\'s wrong with our brain.
    -   Computationally means to understand the subject functions --
        enough to create a replica of them. For example, we don\'t yet
        understand everything about kidneys about we can create
        artificial ones that works well now.
    -   What we know now: very little, but we know some \"constraint\"
        rules
        -   brain component allometry -- relative size of the brain
            components vs overall size. The relationship holds across
            all animal size.
        -   telencephalic uniformity -- neurons throughout the forebrain
            has similar, repeatable designs with only few exceptions.
            This means there is a general representation of a wide
            variety of tasks -- audio, visual , touch etc.
        -   anatomical and physiological imprecision -- the neurons are
            slow and sloppy (probabilistic). However, the brain is
            overall working in a robust way.. how?
        -   task specification -- a classification given freeform input.
            One example is a call support desk. Given a free-form input,
            direct the customer to appropriate channels. It is highly
            contextual and no hard rules applied.
        -   parallel processing -- the neuron circuits are painfully
            slow compared to computer CPU, it seems that the power of
            the brain lies in its massively parrallel computing power.
    -   Current progress
        -   basal ganglia -- this is the area that receive sensory
            input, manage reward and punishments mechanism, and learn
            motor skills. We are close to computationally simulate this.
        -   neocortex -- yeah, no way we are close. Interestingly, the
            neocortex is connected with basal ganglia through a loop. We
            are close to successfully creating all the sensory
            prosthetics, but no way close to simulating the neocortex
            (higher thoughts).
        -   the most exciting area of research today is about how the
            neocortex encode the internal representations of concepts
            and objects.

## Other papers still unassorted

-   \(2017\) [A Joint Many-Task Model: Growing a Neural Network for
    Multiple NLP Tasks](https://openreview.net/forum?id=SJZAb5cel)

    -   ABSTRACT:
        -   Transfer and multi-task learning have traditionally focused
            on either a single source-target pair or very few, similar
            tasks.
        -   Ideally, the linguistic levels of morphology, syntax and
            semantics would benefit each other by being trained in a
            single model. We introduce such a joint many-task model
            together with a strategy for successively growing its depth
            to solve increasingly complex tasks. All layers include
            shortcut connections to both word representations and
            lower-level task predictions.
        -   We use a simple regularization term to allow for optimizing
            all model weights to improve one task's loss without
            exhibiting catastrophic interference of the other tasks. Our
            single end-to-end trainable model obtains state-of-the-art
            results on chunking, dependency parsing, semantic
            relatedness and textual entailment.
        -   It also performs competitively on POS tagging. Our
            dependency parsing layer relies only on a single
            feed-forward pass and does not require a beam search.
    -   This is kind of like Ensembling models, but they are more
        \"joined\" at the end (softmax layer and feature layer), rather
        than just averaging results from softmax.

-   \(2017\) [Hierarchical Memory
    Networks](https://arxiv.org/pdf/1704.03855.pdf)

    -   ABSTRACT:
        -   Memory networks are neural networks with an explicit memory
            component that can be both read and written to by the
            network.
        -   The memory is often addressed in a soft way using a softmax
            function, making end-to-end training with backpropagation
            possible.
        -   However, this is not computationally scalable for
            applications which require the network to read from
            extremely large memories.
        -   On the other hand, it is well known that hard attention
            mechanisms based on reinforcement learning are challenging
            to train successfully.
        -   In this paper, we explore a form of hierarchical memory
            network, which can be considered as a hybrid between hard
            and soft attention memory networks.
        -   The memory is organized in a hierarchical structure such
            that reading from it is done with less computation than soft
            attention over a flat memory, while also being easier to
            train than hard attention over a flat memory.
        -   Specifically, we propose to incorporate Maximum Inner
            Product Search (MIPS) in the training and inference
            procedures for our hierarchical memory network.
        -   We explore the use of various state-of-the art approximate
            MIPS techniques and report results on SimpleQuestions, a
            challenging large scale factoid question answering task.

## Articles and Videos

-   \(2017\) [The End of Human Doctors
    (series)](https://lukeoakdenrayner.wordpress.com/2017/04/20/the-end-of-human-doctors-introduction/)

    -   Part 2: Understanding Medicine
        -   Most of the tasks Medical doctors do are related to
            \"perception\", not \"decision making\". The later part is
            relatively fast and has been done better by the Machine
            since MYCIN.
        -   perceptual tasks like identifying tree-shape patterns in
            X-rays -- Deep learning is very good at it.
        -   Most susceptible specialties are Radiology and Pathology,
            comprising of 25% of doctors (in Australia).
    -   Part 3: Understanding Automation
        -   Automation replaces tasks, not jobs. How much time the task
            takes a human determines how many jobs are lost.
        -   Machines that "help" or "augment" humans still destroy jobs
            and lower wages.
        -   Hybrid-chess does not prove that human/machine teams are
            better than computers alone. STOP SAYING THIS, tech people!
        -   Deep learning threatens tasks that make up a terrifyingly
            large portion of doctors' jobs.
        -   In the developed world, demand for medical services may be
            unable to increase as prices fall due to automation, which
            normally protects jobs.
    -   Part 4: Radiology Escape Velocity
        -   even if the rate of automation of 5% per year, in 30 years
            there will still be one-third the current radiologist
            workforce remaining.
    -   Part 5: Understanding Regulation
        -   In case of USA, it usually takes 3 to 10 years to go through
            the whole process from concept to approval to use in the
            medical industry.
        -   \"measurements\"-related technology can opt to go through
            case-I (low-risk type) route with substantially shorter time
            to approval.
        -   There are two approach in using computer technology
            -   measurements to aid doctors\' decisions. (CADe) --
                doctors disliked them, not doing well as a result.
            -   measurements AND diagnosis (CADx) -- never been approved
                by FDA before.
        -   Conclusion: current regulation in developed countries is
            SUPER conservative and so it will take a lot of time and
            money to get new technology adopted. Not so for developing
            world, we might see it much faster there.
    -   Part 6: Current State-of-the-Art results and impact
        -   Stanford (and collaborators) trained a system to identify
            skin lesions that need a biopsy. Skin cancer is the most
            common malignancy in light-skinned populations.
        -   This is a useful clinical task, and is a large part of
            current dermatological practice.
        -   They used 130,000 skin lesion photographs for training, and
            enriched their training and test sets with more positive
            cases than would be typical clinically.
        -   The images were downsampled heavily, discarding around 90%
            of the pixels.
        -   They used a "tree ontology" to organise the training data,
            allowing them to improve their accuracy by training to
            recognise 757 classes of disease. This even improved their
            results on higher level tasks, like "does this lesion need a
            biopsy?"
        -   They were better than individual dermatologists at
            identifying lesions that needed biopsy, with more true
            positives and less false positives.
        -   While there are possible regulatory issues, the team appears
            to have a working smartphone application already. I would
            expect something like this to be available to consumers in
            the next year or two.
        -   The impact on dermatology is unclear. We could actually see
            shortages of dermatologists as demand for biopsy services
            increases, at least in the short term.

-   \(2017\) [(Video) Geometric Deep Learning - Radcliffe
    Institute](https://www.youtube.com/watch?v=ptcBmEHDWds)

    -   keypoints
        -   Identical twins (Alex & Michael) -- study and worked in the
            same field (Computer Vision)
        -   Invented what became the Kinect camera sensor
        -   Keys for recognizing face:
            -   Humans actually recognize people based on \"texture\"
                appearance, not the 3D geometry
            -   facial expressions changed the projected texture to 2D,
                but not the actual texture if projected on the plane
            -   Therefore, we can use the \"geodesic\" distance instead
                of euclidean distance to measure the actual distance
                between important face features. If the distances are
                approximately the same, then it\'s the same face.
            -   Thee kind of techniques have been use to recognize
                diferent faces, including identical twins.
            -   Geometric deep learning: applying CNNs on 3D surface via
                heat diffusion equation.
                -   Use Case: Recognition, social network analysis,
                    recommender systems

-   \(2015\) [Visual explanation of Information
    Theory](http://colah.github.io/posts/2015-09-Visual-Information/ )

    -   keypoints
        -   Shannon\'s Entropy formula - H(X)
            -   this is a way to estimate how many bits are needed to
                encode given information with certain distributions
            -   the estimated bits are from the best possible encodings
                (\"optimized\")
            -   H(X) = P(X)\*log2(1/P(X)) where P(X) means probabilty of
                X
        -   some interesting permutation give conditional probabilities
            -   P(X,Y) = P(X)\*P(Y\|X) = P(Y)\*P(X\|Y)
            -   H(X,Y) = H(X) + H(Y\|X) = H(Y) + H(X\|Y)
            -   H(X\|Y) = sum{P(X,Y)\*log2(1/P(X\|Y))}
        -   then we can derive \"mutual\" \[I\] and \"variational\"
            \[V\] information
            -   I(X,Y) = H(X,Y) - H(X) - H(Y) = H(X) - H(X\|Y) = H(Y) -
                H(Y\|X)
            -   V(X,Y) = H(X,Y) - I(X,Y)
        -   KL-divergence \[D\] or \[K\]
            -   Dy(x) = K(X\|\|Y) = H(X,Y) - H(X)
            -   This is a way to see how the new distribution (Y) is
                close to the original distribution (X)
            -   if it is the same, then KL is zero, otherwise it has
                value.
            -   this is not a symmetric measure. K(X\|\|Y) \<\>
                K(Y\|\|X)

## Classic Paperspublished before 2012

-   \(2011\) [An analysis of single-layer networks in unsupervised
    feature learning, A. Coates et
    al.](http://machinelearning.wustl.edu/mlpapers/paper_files/AISTATS2011_CoatesNL11.pdf)
-   \(2011\) [Deep sparse rectifier neural networks, X. Glorot et
    al.](http://machinelearning.wustl.edu/mlpapers/paper_files/AISTATS2011_GlorotBB11.pdf)
-   \(2011\) [Natural language processing (almost) from scratch, R.
    Collobert et al.](http://arxiv.org/pdf/1103.0398)
-   \(2010\) [Recurrent neural network based language model, T. Mikolov
    et
    al.](http://www.fit.vutbr.cz/research/groups/speech/servite/2010/rnnlm_mikolov.pdf)
-   \(2010\) [Stacked denoising autoencoders: Learning useful
    representations in a deep network with a local denoising
    criterion, P. Vincent et
    al.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.297.3484&rep=rep1&type=pdf)
-   \(2010\) [Learning mid-level features for recognition, Y.
    Boureau](http://ece.duke.edu/~lcarin/boureau-cvpr-10.pdf)
-   \(2010\) [A practical guide to training restricted boltzmann
    machines, G.
    Hinton](http://www.csri.utoronto.ca/~hinton/absps/guideTR.pdf)
-   \(2010\) [Understanding the difficulty of training deep feedforward
    neural networks, X. Glorot and Y.
    Bengio](http://machinelearning.wustl.edu/mlpapers/paper_files/AISTATS2010_GlorotB10.pdf)
-   \(2010\) [Why does unsupervised pre-training help deep learning, D.
    Erhan et
    al.](http://machinelearning.wustl.edu/mlpapers/paper_files/AISTATS2010_ErhanCBV10.pdf)
-   \(2009\) [Learning deep architectures for AI, Y.
    Bengio.](http://sanghv.com/download/soft/machine%20learning,%20artificial%20intelligence,%20mathematics%20ebooks/ML/learning%20deep%20architectures%20for%20AI%20(2009).pdf)
-   \(2009\) [Convolutional deep belief networks for scalable
    unsupervised learning of hierarchical representations, H. Lee et
    al.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.149.802&rep=rep1&type=pdf)
-   \(2007\) [Greedy layer-wise training of deep networks, Y. Bengio et
    al.](http://machinelearning.wustl.edu/mlpapers/paper_files/NIPS2006_739.pdf)
-   \(2006\) [Reducing the dimensionality of data with neural
    networks, G. Hinton and R.
    Salakhutdinov.](http://homes.mpimf-heidelberg.mpg.de/~mhelmsta/pdf/2006%20Hinton%20Salakhudtkinov%20Science.pdf)
-   \(2006\) [A fast learning algorithm for deep belief nets, G. Hinton
    et
    al.](http://nuyoo.utm.mx/~jjf/rna/A8%20A%20fast%20learning%20algorithm%20for%20deep%20belief%20nets.pdf)
-   \(1998\) [Gradient-based learning applied to document
    recognition, Y. LeCun et
    al.](http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf)
-   \(1997\) [Long short-term memory, S. Hochreiter and J.
    Schmidhuber.](http://www.mitpressjournals.org/doi/pdfplus/10.1162/neco.1997.9.8.1735)

## HW / SW / Dataset

-   \(2016\) [OpenAI gym, G. Brockman et
    al.](https://arxiv.org/pdf/1606.01540)
-   \(2016\) [TensorFlow: Large-scale machine learning on heterogeneous
    distributed systems, M. Abadi et
    al.](http://arxiv.org/pdf/1603.04467)
-   \(2011\) [Torch7: A matlab-like environment for machine learning, R.
    Collobert et
    al.](https://ronan.collobert.com/pub/matos/2011_torch7_nipsw.pdf)
-   \(2015\) [MatConvNet: Convolutional neural networks for matlab, A.
    Vedaldi and K. Lenc](http://arxiv.org/pdf/1412.4564)
-   \(2015\) [Imagenet large scale visual recognition challenge, O.
    Russakovsky et al.](http://arxiv.org/pdf/1409.0575)
-   \(2014\) [Caffe: Convolutional architecture for fast feature
    embedding,Y. Jia et al.](http://arxiv.org/pdf/1408.5093)

## Book / Survey / Review

-   \(2017\) [On the Origin of Deep Learning, H. Wang and Bhiksha
    Raj.](https://arxiv.org/pdf/1702.07800)
-   \(2017\) [Deep Reinforcement Learning: An Overview, Y.
    Li,](http://arxiv.org/pdf/1701.07274v2.pdf)
-   \(2017\) [Neural Machine Translation and Sequence-to-sequence Models
    : A Tutorial, G. Neubig.](http://arxiv.org/pdf/1703.01619v1.pdf)
-   \(2017\) [Neural Network and Deep Learning (Book), Michael
    Nielsen.](http://neuralnetworksanddeeplearning.com/index.html)
-   \(2016\) [Deep learning (Book), Goodfellow et
    al.](http://www.deeplearningbook.org/)
-   \(2016\) [LSTM: A search space odyssey, K. Greff et
    al.](https://arxiv.org/pdf/1503.04069.pdf)
-   \(2016\) [Tutorial on Variational Autoencoders, C.
    Doersch.](https://arxiv.org/pdf/1606.05908)
-   \(2015\) [Deep learning, Y. LeCun, Y. Bengio and G.
    Hinton](https://www.cs.toronto.edu/~hinton/absps/NatureDeepReview.pdf)
-   \(2015\) [Deep learning in neural networks: An overview, J.
    Schmidhuber](http://arxiv.org/pdf/1404.7828)
-   \(2013\) [Representation learning: A review and new perspectives,
    Y.Bengio et al.](http://arxiv.org/pdf/1206.5538)

## Video Lectures / Tutorials / Blogs

### (Lectures)

-   [CS231n, Convolutional Neural Networks for Visual Recognition,
    Stanford University ](http://cs231n.stanford.edu/)
-   [CS224d, Deep Learning for Natural Language Processing, Stanford
    University ](http://cs224d.stanford.edu/)
-   [Oxford Deep NLP 2017, Deep Learning for Natural Language
    Processing](https://github.com/oxford-cs-deepnlp-2017/lectures)

### (Tutorials)

-   [NIPS 2016 Tutorials, Long
    Beach](https://nips.cc/Conferences/2016/Schedule?type=Tutorial)
-   [ICML 2016 Tutorials, New York
    City](http://techtalks.tv/icml/2016/tutorials/)
-   [ICLR 2016 Videos, San Juan
    ](http://videolectures.net/iclr2016_san_juan/)
-   [Deep Learning Summer School 2016,
    Montreal](http://videolectures.net/deeplearning2016_montreal/)
-   [Bay Area Deep Learning School 2016,
    Stanford](https://www.bayareadlschool.org/)

### (Blogs)

-   [OpenAI](https://www.openai.com/)
-   [Distill](http://distill.pub/)
-   [Andrej Karpathy Blog](http://karpathy.github.io/)
-   [Colah\'s Blog](http://colah.github.io/)
-   [WildML](http://www.wildml.com/)
-   [FastML](http://www.fastml.com/)
-   [TheMorningPaper](https://blog.acolyer.org)
