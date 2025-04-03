import { createApp } from 'vue'
import { createPinia } from 'pinia'
import router from './router/index.js'
import { Slider, Upload, Modal, DatePicker, Select, InputNumber, Dropdown, Checkbox, InputPassword, Menu, Input, Table, Card, Drawer, Button, message} from "ant-design-vue"

import axios from 'axios'
window.axios = axios;

import App from './App.vue'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
library.add(fas, fab, far)

import 'ant-design-vue/dist/reset.css'
import 'bootstrap/dist/css/bootstrap-grid.min.css'
import 'bootstrap/dist/css/bootstrap-utilities.min.css'

const pinia = createPinia()
const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(pinia)
app.use(router)
app.use(Card)
app.use(Upload)
app.use(Modal)
app.use(DatePicker)
app.use(Select)
app.use(Dropdown)
app.use(Checkbox)
app.use(Input)
app.use(Menu)
app.use(InputPassword)
app.use(InputNumber)
app.use(Table)
app.use(Drawer)
app.use(Button)
app.use(Slider)
app.mount('#app')

app.config.globalProperties.$message = message