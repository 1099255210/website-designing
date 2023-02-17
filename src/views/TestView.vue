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
    <v-col cols="4">
      <canvas id="main_canvas" width="512" height="512"></canvas>
    </v-col>
    <v-col cols="5">
      <v-card class="mx-auto" max-width="600">
        <v-card-item>
          <v-card-title>属性</v-card-title>
          <v-card-text>
            <v-slider
              v-model="shapeProp.outline"
              label="描边"
              class="align-center"
              :max="constValue.outlineMax"
              :min="constValue.outlineMin"
              :step=".1"
              hide-details
              @update:model-value="changeOutline"
            >
              <template v-slot:append>
                <v-text-field
                  v-model="shapeProp.outline"
                  hide-details
                  single-line
                  density="compact"
                  type="number"
                  style="width: 100px"
                  @input="changeOutline"
                ></v-text-field>
              </template>
            </v-slider>
            <v-slider
              v-model="shapeProp.angle"
              label="旋转"
              class="align-center"
              :max="constValue.angleMax"
              :min="constValue.angleMin"
              :step=".1"
              hide-details
              @update:model-value="changeAngle"
            >
              <template v-slot:append>
                <v-text-field
                  v-model="shapeProp.angle"
                  hide-details
                  single-line
                  density="compact"
                  type="number"
                  style="width: 100px"
                  @input="changeAngle"
                ></v-text-field>
              </template>
            </v-slider>
          </v-card-text>
          <v-divider></v-divider>
          <v-card-title>管理元素</v-card-title>
          <v-card-actions>
            <v-btn variant="outlined" @click="addRect">矩形</v-btn>
            <v-btn variant="outlined" @click="addCircle">圆形</v-btn>
            <v-btn variant="outlined" @click="addTri">三角形</v-btn>
            <v-btn variant="outlined" @click="addTextBox">文字</v-btn>
            <v-btn variant="outlined" @click="deleteObj">删除</v-btn>
          </v-card-actions>
          <v-file-input label="上传图片" variant="underlined"></v-file-input>
          <v-divider></v-divider>
          <v-card-title>导出项目</v-card-title>
          <v-card-actions>
            <v-btn variant="outlined" @click="downloadPNG">导出为PNG</v-btn>
            <v-btn variant="outlined" @click="downloadJSON">导出为Json</v-btn>
          </v-card-actions>
          
        </v-card-item>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  data() {
    return {
      message: "",
      imageFile: "",
      shapeProp: {
        outline: 0,
        outlineColor: '#00ffff',
        angle: 0,
        left: 0,
        top: 0,
      },
      textProp: {
        outline: 0,
        angle: 0,
        left: 0,
        top: 0,
        font: "",
      },
      constValue: {
        outlineMin: 0,
        outlineMax: 20,
        angleMin: 0,
        angleMax: 360,
      },
      
    };
  },
  methods: {
    /*
     * Canvas init and boundingbox customize
     */
    initCanvas() {
      this.canvas = new fabric.Canvas("main_canvas", {
        backgroundColor: "white",
        selectionBorderColor: "#979797",
        selectionColor: "transparent",
        selectionDashArray: [4, 4],
        selectionLineWidth: 1,
      })
      this.canvas.on('mouse:down', function(options) {
        if (options.target) {
          console.log('an object was clicked! ', options.target.type);
        }
      });
      this.canvas.on('selection:created', function(options) {
        if (options.selected.length == 1) {
          console.log('selected one obj');
        }
      })
    },
    redefineBB(obj) {
      obj.set({
        borderColor: "black",
        cornerColor: "black",
        cornerSize: 5,
        transparentCorners: false,
      });
    },
    updateProp() {
      var obj = this.canvas.getActiveObject()
      this.shapeProp.outlineColor = obj.stroke
      this.shapeProp.outline = obj.strokeWidth
      this.shapeProp.angle = obj.angle
    },

    /**
     * Change Properties.
     */
    changeOutline() {
      var obj = this.canvas.getActiveObject()
      obj.set('strokeWidth', parseFloat(this.shapeProp.outline)).setCoords()
      obj.set('stroke', this.shapeProp.outlineColor)
      this.canvas.requestRenderAll()
      console.log(obj.stroke)
    },
    changeAngle() {
      var obj = this.canvas.getActiveObject()
      obj.set('angle', parseFloat(this.shapeProp.angle)).setCoords()
      this.canvas.requestRenderAll()
    },
    deleteObj() {
      var obj = this.canvas.getActiveObject()
      this.canvas.remove(obj)
    },

    /*
     * Add objects.
     */
    addRect() {
      var rect = new fabric.Rect({
        top: 50,
        left: 50,
        width: 100,
        height: 100,
        stroke: 'black',
        strokeWidth: 0,
        fill: "black",
      });
      this.redefineBB(rect);
      this.canvas.add(rect);
    },
    addCircle() {
      var circle = new fabric.Circle({
        top: 50,
        left: 50,
        radius: 100,
        stroke: 'black',
        strokeWidth: 0,
        fill: "black",
      });
      this.redefineBB(circle);
      this.canvas.add(circle);
    },
    addTri() {
      var tri = new fabric.Triangle({
        top: 50,
        left: 50,
        width: 100,
        height: 100,
        stroke: 'black',
        strokeWidth: 0,
        fill: "black",
      });
      this.redefineBB(tri);
      this.canvas.add(tri);
    },
    addTextBox() {
      var tb = new fabric.Textbox("Typehere", {
        left: 50,
        top: 50,
        fontSize: 50,
      });
      this.redefineBB(tb);
      this.canvas.add(tb);
    },
    uploadImage() {

    },

    /*
     * Dump canvas.
     */
    downloadPNG() {
      var base64 = this.canvas.toDataURL({
        format: "png",
        enableRetinaScaling: false,
      });
      var filename = new Date().getTime().toString() + ".png";
      var link = document.createElement("a");
      link.href = base64;
      link.download = filename;
      link.click();
      URL.revokeObjectURL(link.href);
    },
    downloadJSON() {
      var file = new Blob([JSON.stringify(this.canvas, null, "\t")], {
        type: "text/plain",
      })
      var filename = new Date().getTime().toString() + ".json";
      var link = document.createElement("a");
      link.href = URL.createObjectURL(file);
      link.download = filename;
      link.click();
    },
    loadJSON() {
      this.canvas.loadFromJSON();
    },
  },
  mounted() {
    this.initCanvas();
  },
};
</script>
