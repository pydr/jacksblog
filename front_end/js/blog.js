// 格式化时间输出
Vue.filter('Date',function(value){
    var d = new Date(value);
       var year = d.getFullYear();
       var month = d.getMonth() + 1;
       var day = d.getDate() <10 ? '0' + d.getDate() : '' + d.getDate();
       var hour = d.getHours();
       var minutes = d.getMinutes();
       var seconds = d.getSeconds();
       var eng_month = ""
       if(month==1){
           eng_month = "Jan"
       }else if(month==2){
           eng_month = "Feb"
       }else if(month==3){
           eng_month = "Mar"
       }else if(month==4){
           eng_month = "Apr"
       }else if(month==5){
           eng_month = "May"
       }else if(month==6){
           eng_month = "Jun"
       }else if(month==7){
           eng_month = "Jul"
       }else if(month==8){
           eng_month = "Aug"
       }else if(month==9){
           eng_month = "Sep"
       }else if(month==10){
           eng_month = "Oct"
       }else if(month==11){
           eng_month = "Nov"
       }else if(month==12){
           eng_month = "Dec"
       }
       return  eng_month + ' ' + day + ', ' + year;
});


// BreakingNews Bar Data
var vm = new Vue({
    el: "#breaking",
    delimiters: ['[[', ']]'],
    data: {
        host,
        recent_post: [],
    },

    mounted: function(){
	    this.get_recent_post();
    },

    methods: {

        get_recent_post: function(){
            // 获取最近更新文章列表
            axios.get(this.host + 'recent_posts/', {
                responseType: 'json',
            }).then(response=>{
                this.recent_post = response.data;
            }).catch(error=>{
                console.log("request recent posts failed")
            })
        },

    }
});


// side bar function
var vm4 = new Vue({
    el: "#side",
    delimiters: ['[[', ']]'],
    data: {
        host,
        email: "",
        email_message: "",
        message_style: "",
        popular_post_list: [],
        recent_posts_list: [],
        check: true,
    },
    mounted: function(){
        this.get_popular_post_list();
        this.get_recent_posts();
    },
    methods: {
        check_email: function(){
            var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;
            if (!this.email) {
                this.email_message = "请输入Email地址!";
                this.message_style = "red";
                this.check = false;
                return;
            }else if( !re.test(this.email)){
                this.email_message = "Email格式不正确！";
                this.message_style = "red";
                this.check = false;
                return;
            }
            this.check = true;
        },
        doSubmit: function(e){
            e.preventDefault();
            this.check_email();
            if (this.check){
                axios.post(this.host + "subscribe/", {
                email: this.email
                },{
                    responseType: 'json'
                },).then(response=>{
                    this.email_message = "订阅成功！";
                    this.message_style = "green";
                }).catch(error=>{
                    this.email_message = "您已订阅过本站，无需重复订阅";
                    this.message_style = "red";
                })
            }
        },

        get_popular_post_list: function(){
            // 获取最受欢迎文章列表
            axios.get(this.host + 'popular_post/', {
                responseType: 'json',
            }).then(response=>{
                this.popular_post_list = response.data;
            }).catch(error=>{
                console.log("request failed")
            })
        },

        get_recent_posts: function(){
            // 获取最近更新文章列表
            axios.get(this.host + 'recent_posts/', {
                responseType: 'json',
            }).then(response=>{
                this.recent_posts_list = response.data;
            }).catch(error=>{
                console.log("request failed")
            })
        },
    }
});


var page = 0; // 当前页
var limit = 5;
var ordering = "-update_time";
var total_page = 1;  // 总页数
var data_querying = true;   // 是否正在向后台获取数据
var is_get=true;
var host = "http://127.0.0.1:8000/";

$(function () {
    // get Home page list data
    vm2 = new Vue({
        el: "#list",
        delimiters: ['[[', ']]'],
        data: {
            host,
            posts_list: [],
        },

    });
    get_blog_list();

    //页面滚动加载相关
    $(window).scroll(function () {
        // 浏览器窗口高度
        var showHeight = $(window).height();
        // 整个网页的高度
        var pageHeight = $(document).height();
        // 页面可以滚动的距离
        var canScrollHeight = pageHeight - showHeight;
        // 页面滚动了多少,这个是随着页面滚动实时变化的
        var nowScroll = $(document).scrollTop();
        if ((canScrollHeight - nowScroll) < 100 && is_get) {
            // TODO 判断页数，去更新新闻数据
            get_blog_list();
        }
    })
});
function get_blog_list() {
    // TODO 更新新闻数据
    is_get=false;
    $.get(host + 'blog/post',{
        //传递要加载第几页的数据
        page: page + 1,
        limit: limit,
        ordering: ordering

    },function (data) {
        //data==>{news_list:[{},{},...]}
        //将原数据与新数据拼成一个更大的数据数组
        //修改当前的页码值
        if(data.results.length>0) {
            //如果是在请求第一页数据，则直接赋值
            //如果是在请求非第一页数据，则拼接
            page++;
            if (page == 1) {
                vm2.posts_list = data.results;
            } else {
                vm2.posts_list = vm2.posts_list.concat(data.results);
            }

            if (data.next == null){
                is_get = false;
            }else{
                is_get = true;
            }
        }
    });
}


