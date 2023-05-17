<script setup>
import axios from 'axios'
axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
</script>

<script>

import { onMounted, ref } from 'vue'

export default {
  setup() {
    const fileInput = ref(null);

    onMounted(() => {
      console.dir(fileInput.value);
    });

    return {
      fileInput
    };
  }
}

</script>

<template>
  <v-row>
    <v-col cols="3">
      <v-card class="mx-auto" max-width="344" variant="outlined">
        <v-card-item>
          <div class="text-overline mb-1">商品海报生成测试</div>
          <div class="text-h6 mb-1">商品海报生成测试</div>
        </v-card-item>
      </v-card>
    </v-col>
    <v-col cols="4">
      <input type="file" ref="fileInput" @change="onFileInputChange" />
      <button onclick="onFileInputChange">点击</button>
    </v-col>
    <v-col cols="5">
      <v-img
        :width="300"
        aspect-ratio="16/9"
        cover
        :src="imageData"
      ></v-img>
    </v-col>
  </v-row>
</template>