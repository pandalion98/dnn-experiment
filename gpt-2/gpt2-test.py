from os import environ
import gpt_2_simple as gpt2

#gpt2.download_gpt2(model_name="124M")
environ['CUDA_VISIBLE_DEVICES'] = '-1'

sess = gpt2.start_tf_sess()

gpt2.finetune(sess,
              dataset='arxiv-titles.txt',
              model_name='124M',
              steps=1000,
              restore_from='fresh',
              run_name='run1',
              print_every=1,
              sample_every=20,
              save_every=20
              )
