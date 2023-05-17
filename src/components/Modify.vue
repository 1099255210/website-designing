<script setup>
import axios from "axios";
import { fabric } from 'fabric'
import 'fabric-history';
axios.defaults.headers.post["Access-Control-Allow-Origin"] = "*";
</script>

<template>
  <v-row>
    <v-col cols="10">
      <img class="thumbnail-img" :src="thumbnailImage" @click="renderCanvasFromThumbnail" />
    </v-col>
    <v-col cols="2">
      留白
    </v-col>
  </v-row>
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
      <div class="d-flex" style="width: 515px; height: 752px; border-color: black; border: solid 1px; background-color: antiquewhite;">
        <canvas id="main_canvas" width="513" height="750"></canvas>
      </div>
    </v-col>
    <v-col cols="4">
      <v-card class="mx-auto" max-width="600">
        <v-card-item>
          <v-card-title>图形属性</v-card-title>
          <v-card-text>
            <v-slider
              v-model="shapeProp.outline"
              label="描边"
              class="align-center"
              :max="constValue.outlineMax"
              :min="constValue.outlineMin"
              :step=".1"
              hide-details
              :disabled="!shapePropValid"
            >
              <template v-slot:append>
                <v-text-field
                  v-model="shapeProp.outline"
                  hide-details
                  single-line
                  density="compact"
                  type="number"
                  style="width: 100px"
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
              :disabled="!shapePropValid"
            >
              <template v-slot:append>
                <v-text-field
                  v-model="shapeProp.angle"
                  hide-details
                  single-line
                  density="compact"
                  type="number"
                  style="width: 100px"
                ></v-text-field>
              </template>
            </v-slider>

            <div class="color-tool">
              选择边框颜色
              <span class="color-box" :style="'background-color: ' + shapeProp.outlineColor" @click="toggleOutlineColorPicker()"></span>
              <v-card class="color-picker" v-if="outlineColorDisplay" v-click-outside="hideOutlineColorPicker">
                <v-card-item>
                  <v-color-picker
                    v-model="shapeProp.outlineColor"
                    :mode="colorMode"
                  >
                  </v-color-picker>
                  <v-divider></v-divider>
                  <v-btn-toggle v-model="colorMode" v-if="outlineColorDisplay" mandatory>
                    <v-btn v-for="(item, index) in constValue.colorModes" :key="index" :value="item">{{ item }}</v-btn>
                  </v-btn-toggle>
                </v-card-item>
              </v-card>
            </div>

          </v-card-text>
          <v-divider></v-divider>

          <v-card-title>文字属性</v-card-title>
          <v-card-actions>
            <v-btn variant="outlined" @click="addTextBox">文字</v-btn>
            <v-select
              v-model="fontFamilySelected"
              :items="fontFamilyList"
            ></v-select>
            <v-btn variant="outlined" :disabled="!textPropValid" @click="changeFontWeight">加粗</v-btn>
            <v-btn variant="outlined" :disabled="!textPropValid" @click="changeFontStyle">斜体</v-btn>
          </v-card-actions>
          <v-divider></v-divider>

          <v-card-title>添加元素</v-card-title>
          <v-card-actions>
            <v-btn variant="outlined" @click="addRect">矩形</v-btn>
            <v-btn variant="outlined" @click="addCircle">圆形</v-btn>
            <v-btn variant="outlined" @click="addTri">三角形</v-btn>
          </v-card-actions>
          <v-card-actions>
            <input id="imageInput" type="file" accept="image/jpeg, image/png, image/jpg" v-show="false">
            <v-btn variant="outlined" @click="uploadImage">上传图片</v-btn>
          </v-card-actions>
          <v-divider></v-divider>

          <v-card-title>项目</v-card-title>
          <v-card-actions>
            <input id="JSONInput" type="file" v-show="false">
            <v-btn variant="outlined" @click="importJSON">导入项目</v-btn>
            <v-btn variant="outlined" @click="downloadPNG">导出为PNG</v-btn>
            <v-btn variant="outlined" @click="downloadJSON">导出为Json</v-btn>
            <v-btn variant="outlined" @click="exportToTimeline">导出至时间线</v-btn>
          </v-card-actions>

          <v-card-title>操作</v-card-title>
          <v-card-actions>
            <v-btn variant="outlined" @click="canvasUndo">撤销</v-btn>
            <v-btn variant="outlined" @click="deleteObj">删除</v-btn>
            <v-btn variant="outlined" @click="showConfirmationDialog = true">清除画板</v-btn>
            <v-dialog v-model="showConfirmationDialog" max-width="400">
              <v-card>
                <v-card-title class="headline">确认清除画板</v-card-title>
                <v-card-text>确定要清除画板吗？这将删除画板上的所有内容。</v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn text @click="showConfirmationDialog = false">取消</v-btn>
                  <v-btn color="error" text @click="clearCanvasAndCloseDialog">清除</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
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
      thumbnailImage: '',
      colorMode: "rgba",
      fontFamilySelected: "Default",
      fontFamilyList: [
        "Default",
        "Quicksand",
        "Neon Sans",
        "Qing Ke",
        "SourceHanSans-Bold"
      ],
      fillColorPropValid: false,
      fillColorDisplay: false,
      outlineColorPropValid: false,
      outlineColorDisplay: false,
      shapeType: ["rect", "circle", "triangle", "image"],
      shapePropValid: false,
      shapeProp: {
        outline: 0,
        fillColor: "#000000",
        outlineColor: "#000000",
        angle: 0,
        left: 0,
        top: 0,
      },
      fontFamily: "Times New Roman",
      textPropValid: false,
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
        colorModes: ["rgba", "hexa", "hex"],
      },
      showConfirmationDialog: false,

    };
  },
  watch: {
    shapeProp: {
      handler(newValue, oldValue) {
        console.log(newValue, oldValue)
        var obj = this.canvas.getActiveObject()
        if (obj) {
          obj.stroke = newValue.outlineColor
          obj.strokeWidth = newValue.outline
          obj.angle = newValue.angle
          this.canvas.requestRenderAll()
          // this.canvas.renderAll()
        }
      },
      deep: true
    }
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
      this.canvas.on('mouse:down', (e) => {
        if (e.target) {
          this.redefineBB(e.target)
          this.redefineObjCaching(e.target)
        } else {
          this.shapePropValid = false
          this.textPropValid = false
        }
      });
      this.canvas.on('selection:created', (e) => {
        this.updatePropSetting(e)
      })
      this.canvas.on('selection:updated', (e) => {
        this.updatePropSetting(e)
      })
      this.canvas.on('object:rotating', (e) => {
        this.updateProp(e)
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
    redefineObjCaching(obj) {
      obj.set('objectCaching', false);
    },
    updateProp(e) {
      var obj = this.canvas.getActiveObject()
      this.shapeProp.outlineColor = obj.stroke
      this.shapeProp.outline = obj.strokeWidth
      this.shapeProp.angle = obj.angle
      console.log(obj.stroke, obj.strokeWidth, obj.angle)
    },
    updatePropSetting(e) {
      console.log(e)
      // Todo: change selection border
      if (e.selected.length == 1) {
        if (this.shapeType.includes(e.selected[0].type)) {
          this.shapePropValid = true
          this.textPropValid = false
          this.updateProp()
        } else if (e.selected[0].type == "textbox") {
          this.shapePropValid = false
          this.textPropValid = true
          this.updateProp()
        } 
        else {
          this.shapePropValid = false
          this.textPropValid = false
        }
      } 
    },
    initImageUploader() {
      document.getElementById("imageInput").onchange = (e) => {
        var reader = new FileReader()
        reader.onload = (f) => {
          var imgObj = new Image()
          imgObj.src = f.target.result
          imgObj.onload = () => {
            var image = new fabric.Image(imgObj)
            image.set({
              angle: 0,
              weight: imgObj.width,
              height: imgObj.height,
            });
            this.redefineBB(image)
            this.canvas.centerObject(image).add(image).renderAll()
          }
        }
        reader.readAsDataURL(e.target.files[0])
      }
    },
    initJSONUploader() {
      document.getElementById("JSONInput").onchange = (e) => {
        var reader = new FileReader()
        reader.onload = (f) => {
          this.canvas.loadFromJSON(f.target.result)
        }
        reader.readAsText(e.target.files[0])
      }
    },
    initKeyboardEvent() {
      document.onkeydown = (e) => {
        
        if (e.key == "Delete") {
          this.deleteObj()
        } else if (e.ctrlKey && e.key === 'z') {
          this.canvas.undo()
        } else if (e.ctrlKey && e.key === 's') {
          console.log("save")
          // Todo: save status
        }
        // Todo: redo
      }
    },

    /**
     * Some Global Opration
     */
    canvasUndo() {
      this.canvas.undo()
    },
    canvasClean() {
      this.canvas.clear()
      this.canvas.backgroundColor = 'white';
    },

    /**
     * Dialog Cleaner
     */

    clearCanvasAndCloseDialog() {
      setTimeout(() => {
        this.canvasClean()
        this.showConfirmationDialog = false
      }, 100)
    },

    /**
     * Tools Settings.
     */
    toggleFillColorPicker() {
      this.fillColorDisplay = !this.fillColorDisplay
    },
    toggleOutlineColorPicker() {
      this.outlineColorDisplay = !this.outlineColorDisplay
    },
    hideOutlineColorPicker() {
      this.outlineColorDisplay = false
    },
    

    /**
     * Change Properties.
     */
    changeFontWeight() {

    },
    changeFontSize() {

    },
    changeFontStyle() {

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
      rect.set('objectCaching', false)
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
      circle.set('objectCaching', false)
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
      tri.set('objectCaching', false)
      this.canvas.add(tri);
    },
    addTextBox() {
      if (this.fontFamilySelected == "Default") {
        this.fontFamily = "Times New Roman"
      } else {
        this.fontFamily = this.fontFamilySelected
      }
      var tb = new fabric.Textbox("输入文字 Text", {
        left: 50,
        top: 50,
        fontSize: 50,
        fontFamily: this.fontFamily,
      });
      tb.set('objectCaching', false)
      this.canvas.add(tb).renderAll();

    },
    uploadImage() {
      document.getElementById("imageInput").click();
    },

    /*
     * Dump and import canvas.
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
    importJSON() {
      document.getElementById("JSONInput").click();
    },
    exportToTimeline() {
      const imageData = this.canvas.toDataURL({ format: 'png' });
      const jsonData = JSON.stringify(this.canvas.toJSON());
      this.thumbnailImage = imageData;

      // 创建下载链接并保存JSON文件
      const jsonLink = document.createElement('a');
      const blob = new Blob([jsonData], { type: 'application/json' });
      jsonLink.href = URL.createObjectURL(blob);
      jsonLink.download = 'canvas.json';
      jsonLink.click();
    },
    renderCanvasFromThumbnail() {
      fetch('canvas.json')
        .then(response => response.json())
        .then(jsonData => {
          this.canvas.clear();
          this.canvas.loadFromJSON(jsonData, () => {
            this.canvas.renderAll();
          });
        });
    },
    renderCanvas() {
      // 发送请求获取JSON布局数据
      axios.get('/layout')
        .then(response => {
          const layoutData = response.data;
          this.canvas.loadFromJSON(layoutData)
        })
        .catch(error => {
          console.error(error);
        });
    },
    getThumbnail() {
      axios.get('/thumbnail')
        .then(response => {
          this.thumbnail = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
  },
  mounted() {
    this.initCanvas()
    this.initImageUploader()
    this.initJSONUploader()
    this.initKeyboardEvent()
  },
};
</script>

<style scoped>
.color-box {
  display: inline-block;
	width: 16px;
	height: 16px;
	background-color: #fff;
	cursor: pointer;
}
.color-tool {
  position: relative;
}
.color-picker {
  position: absolute;
  top: 20px;
  left: 0;
  z-index: 9;
}

.thumbnail-img {
  cursor: pointer;
  height: 200px; /* 设置图片高度 */
}
</style>