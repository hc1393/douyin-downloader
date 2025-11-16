function get_time(page){
    var var0 = page,var1=Math.ceil(new Date().getTime() / 1000);
    result = var0 + Math.floor(var1 / 3) + 16358
    return [result,var1]
}
