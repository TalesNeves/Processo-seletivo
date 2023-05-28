<template>
   <div>
    <div class="card withpadding">
       <input style="background-color: #fffdd1;" placeholder="Razão Social" v-model="data.lookforterm" type="text" class="form-control"/>
       <div class="withpadding">

         <button @click="getByRazao" type="button" class="btn btn-primary">Procurar</button>
       </div>
      <div class="card-header">
        <h4>
          Operadoras

        </h4>
      </div>
      <div class="absolute table-responsive card-body">
        <table style="table-layout: fixed;" class="table-hover table-striped table-bordered">
          <thead>
           <tr>
        <th>reg_ans</th>
        <th>cnpj</th>
        <th>razao_social</th>
        <th>nome_fantasia </th>
        <th>modalidade</th>
        <th>logradouro</th>
        <th>numero</th>
        <th>complemento</th>
        <th>bairro</th>
        <th>cidade</th>
        <th>uf</th>
        <th>cep</th>
        <th>ddd</th>
        <th>telefone</th>
        <th>fax</th>
        <th>email</th>
        <th>representante</th>
        <th>cargo_representant</th>
        <th>data_registro_ans</th>
        
            </tr>
          </thead>
          <tbody>
            <tr  v-for="(operadora,index) in this.data.operadoras" :key="index">
        <td class="lastcell" style="white-space: nowrap; text-overflow: ellipsis; overflow: hidden;"  >{{operadora.reg_ans}}</td>
        <td class="lastcell" style="white-space: nowrap; text-overflow: ellipsis; overflow: hidden;"  >{{operadora.razao_social}}</td>
        <td class="lastcell" style="white-space: nowrap; text-overflow: ellipsis; overflow: hidden;"  >{{operadora.cnpj}}</td>
        <td class="lastcell" style="white-space: nowrap; text-overflow: ellipsis; overflow: hidden;"  >{{operadora.nome_fantasia }}</td>
        <td class="lastcell" style="white-space: nowrap; text-overflow: ellipsis; overflow: hidden;"  >{{operadora.modalidade}}</td>
        <td class="lastcell" style="white-space: nowrap; text-overflow: ellipsis; overflow: hidden;"  >{{operadora.logradouro}}</td>
        <td class="lastcell" style="white-space: nowrap; text-overflow: ellipsis; overflow: hidden;"  >{{operadora.numero}}</td>
        <td class="lastcell" style="white-space: nowrap; text-overflow: ellipsis; overflow: hidden;"  >{{operadora.complemento}}</td>
        <td class="lastcell" style="white-space: nowrap; text-overflow: ellipsis; overflow: hidden;"  >{{operadora.bairro}}</td>
        <td class="lastcell" style="white-space: nowrap; text-overflow: ellipsis; overflow: hidden;"  >{{operadora.cidade}}</td>
        <td class="lastcell" style="white-space: nowrap; text-overflow: ellipsis; overflow: hidden;"  >{{operadora.uf}}</td>
        <td class="lastcell" style="white-space: nowrap; text-overflow: ellipsis; overflow: hidden;"  >{{operadora.cep}}</td>
        <td class="lastcell" style="white-space: nowrap; text-overflow: ellipsis; overflow: hidden;"  >{{operadora.ddd}}</td>
        <td class="lastcell" style="white-space: nowrap; text-overflow: ellipsis; overflow: hidden;"  >{{operadora.telefone}}</td>
        <td class="lastcell" style="white-space: nowrap; text-overflow: ellipsis; overflow: hidden;"  >{{operadora.fax}}</td>
        <td class="lastcell" style="white-space: nowrap; text-overflow: ellipsis; overflow: hidden;"  >{{operadora.email}}</td>
        <td class="lastcell" style="white-space: nowrap; text-overflow: ellipsis; overflow: hidden;"  >{{operadora.representante}}</td>
        <td class="lastcell" style="white-space: nowrap; text-overflow: ellipsis; overflow: hidden;"  >{{operadora.cargo_representant}}</td>
        <td class="lastcell" style="white-space: nowrap; text-overflow: ellipsis; overflow: hidden;"  >{{operadora.data_registro_ans}}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
   </div>
  
</template>

<script>
import axios from 'axios'

export default{

  name: 'operadoras',
  data(){
    return{
    
      data:{
        operadoras: [],
        lookforterm: ""
      }
        
    }
  },
  mounted(){
    this.getOperadoras();
  },
  methods:{
    getOperadoras(){
      axios.get('http://ec2-18-118-189-190.us-east-2.compute.amazonaws.com:5000/all').then(res => {
        this.data.operadoras = res.data
      });
    },
    getByRazao(){
      axios.get('http://ec2-18-118-189-190.us-east-2.compute.amazonaws.com:5000/like/'+this.data.lookforterm).then(res => {
        this.data.operadoras = res.data
      });
    }
  }
}
</script>

<style>
.withpadding {
  padding: 5px
}
td {
  border: 1px solid black;
}
.lastcell {
  max-width: 10px;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
  /* transition: 0.1s; */
}

.lastcell:hover {
  position: absolute;
  background-color: yellow;
  max-width: 1000px;
  padding: 4px;
}

.lastrow:hover{
  position: absolute;
  background-color: yellow;
  max-width: 1000px;
  padding: 4px;
}

.lastrow:hover{
  position: absolute;
  background-color: yellow;
  max-width: 1000px;
  padding: 4px;
}

.col:hover {
  flex-grow: 5;
  transition: flex-grow .3s;
  -webkit-transition: flex-grow .3s;
}
.table-responsive::-webkit-scrollbar {
    -webkit-appearance: none;
}

.table-responsive::-webkit-scrollbar:vertical {
    width: 12px;
}

.table-responsive::-webkit-scrollbar:horizontal {
    height: 12px;
}

.table-responsive::-webkit-scrollbar-thumb {
    background-color: rgba(0, 0, 0, .5);
    border-radius: 10px;
    border: 2px solid #ffffff;
}

.table-responsive::-webkit-scrollbar-track {
    border-radius: 10px;  
    background-color: #ffffff; 
}
table {
        width: 100%;
    }


/* tbody { display: flex; } */

/* tr:after {
    content: ' ';
    display: block;
    visibility: hidden;
    clear: both;
}

thead th {
    height: 30px;

    /*text-align: left;*/


/* tbody {
    height: 220px;
    overflow-y: auto;
} */




/* thead th {
    width: 19.5%;
    float: left;
}
tbody td {
    width: 20%;
    float: left;
} */ 

/* .table-responsive {
 /* height: 100vh; */
 /* width: 100vw; */
 /* overflow: auto; */

</style>