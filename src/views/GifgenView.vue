<script setup>
import Gifshow from '../components/Gifshow.vue'
import axios from 'axios'
axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
</script>

<script>
export default {
  data () {
    return {
      link: 'Image',
    }
  },
  methods: {
    async sub(credentials) {
      const res = await axios.post('/api/gifgen', credentials)
      console.log(res['data'])
      this.link = res['data']
    },
  }
}
</script>

<template>
  <v-row>
    <v-col cols="3">
      <v-card class="mx-auto" max-width="344" variant="outlined">
        <v-card-item>
          <div class="text-overline mb-1">GIF poster</div>
          <div class="text-h6 mb-1">动态海报生成</div>
        </v-card-item>
      </v-card>
    </v-col>
    <v-col cols="4">
      <FormKit
        type="form"
        :value="{
          words: 'Coffee\nBAR\nKTV',
          direction: 'rtl',
        }"
        id="sample"
        @submit="sub"
      >
        <h1>动态海报生成</h1>
        <br>
        <p>输入你的广告词，选择合适的选项，生成灯牌风格的动态海报！</p>
        <br>
        <FormKit
          type="textarea"
          name="words"
          label="广告词"
          help="输入广告词/句，一行一个"
          validation="required"
        />

        <FormKit
          type="radio"
          name="direction"
          label="方向"
          help="生成文字的方向"
          :options="{
            rtl: '从左到右',
            ttb: '从上到下',
            random: '随机'
          }"
        />

        <FormKit
          type="text"
          name="duration"
          label="时长"
          help="生成动态海报的时长"
          placeholder="单位:秒（默认为5）"
        />
      </FormKit>
    </v-col>
    <v-col cols="5">
      <Gifshow :link="link" :key="componentKey"/>
    </v-col>
  </v-row>
</template>