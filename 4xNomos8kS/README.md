Status: In Progress

Using x4plus as a pretrain, finetuning it on musls Nomos8k_sfw, a 4x model on RRDBNet, gt_size: 256, batch_size 10, GPU P100

8kS - trained for 12 hours, l1_gt_usm: True and percept_gt_usm: True with small otf degradation values.

8kSC - trained for 12 hours, l1_gt_usm: False and precept_gt_usm: False and only otf compression and blur degradations, no noise.