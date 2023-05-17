<script setup>
import axios from "axios";
axios.defaults.headers.post["Access-Control-Allow-Origin"] = "*";
</script>

<template>
  <v-row>
    <v-col cols="3">
      <v-card class="mx-auto" max-width="344" variant="outlined">
        <v-card-item>
          <div class="text-overline mb-1">Test</div>
          <div class="text-h6 mb-1">测试功能</div>
        </v-card-item>
      </v-card>
    </v-col>
    <v-col cols="5">
      <div class="d-flex" style="width: 702px; height: 702px; border-color: black; border: solid 1px;">
        <input id="imageInput" type="file" accept="image/jpeg, image/png, image/jpg" v-show="false">
        
        <v-btn variant="outlined" @click="uploadImage">上传图片</v-btn>
      </div>
    </v-col>
    <v-col cols="4">
      <v-card class="mx-auto" max-width="600">
      </v-card>
    </v-col>
  </v-row>
</template>