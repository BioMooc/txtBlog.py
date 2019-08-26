/**
 * startMove 原生JS运动库，支持匀速、减速和弹性运动三种运动方式
 * @author richard chen
 * @update 2014-09-17
 * @version 1.0
 * @参数 opt {}
 *     obj: 要运动的元素
 *     json: 要改变的属性
 *     effect: 运动方式：linear匀速，easeOut减速，easeInOut弹性，默认为linear
 *     iSpeed: 每次运动的步长，默认为10
 *     fn: 运动完成的回调
 */
function startMove(obj, json, effect, iSpeed, fn) {
    return new startMove.prototype.init(obj, json, effect, iSpeed, fn);
}
startMove.prototype.start = function() {
    var iCur,
        _this = this;
    
    clearInterval(this.obj.timer);
    this.obj.timer = setInterval(function() {
        var flag = true, // 运动完成标志
            step; // 每次运动步长
            
        for(var attr in _this.json) {
            if(attr == "opacity") {
                iCur = Math.round(_this.getStyle(_this.obj, attr) * 100);
            } else {
                iCur = parseInt(_this.getStyle(_this.obj, attr));
            }
            
            // 计算步长
            step = _this[_this.effect](iCur, attr);
            
            if(attr == "opacity") {
                _this.obj.style[attr] = (iCur + step) / 100;
                _this.obj.style.filter = "alpha(opacity=" + (iCur + step) + ");";
            } else {
                _this.obj.style[attr] = iCur + step + "px";
            }
            
            
            if(iCur != _this.json[attr]) {
                flag = false;
            }
        }
        
        if(flag) {
            clearInterval(_this.obj.timer);
            _this.fn && _this.fn.call(_this.obj);
        }
    }, 30);
};
startMove.prototype.linear = function(iCur, attr) {
    var iTarget = this.json[attr];
    var step = this.speed;
    
    step = iCur > iTarget ? -step : step;
    if(step > 0 && (iCur + step > iTarget)) {
        step = iTarget - iCur;
    } else if (step < 0 && (iCur + step) < iTarget) {
        step = iTarget - (iCur + step);
    }
    
    return step;
};
startMove.prototype.easeOut = function(iCur, attr) {
    var iTarget = this.json[attr];
    var step = (iTarget - iCur) / 8;
    step = step > 0 ? Math.ceil(step) : Math.floor(step);
    return step;
};
startMove.prototype.easeInOut = function(iCur, attr) {
    var iTarget = this.json[attr],
        // 为每个要改变的属性声明一个step属性
        step = attr + "_step";
    
    // 初始化step属性
    if(!this[step]) {
        this[step] = 0;
    }
    
    this[step] += (iTarget - iCur) / 8;
    this[step] = this[step] * 0.75;
    this[step] = this[step] > 0 ? Math.ceil(this[step]) : Math.floor(this[step]);
    
    // 当step接近一个最小值，并且当前位置离目标位置接近一个最小值，说明运动趋于完成
    if(Math.abs(this[step]) <= 3 && Math.abs(iTarget - iCur) <= 3) {
        this[step] = iTarget - iCur;
    }
    return this[step];
};
startMove.prototype.getStyle = function (obj, attr) {
    if(obj.currentStyle) {
        return obj.currentStyle[attr];
    } else {
        return getComputedStyle(obj, false)[attr];
    }
};
startMove.prototype.init = function(obj, json, effect, iSpeed, fn) {
    this.obj = obj;
    this.json = json;
    this.effect = effect || "linear";
    this.speed = iSpeed || 10;
    this.fn = fn;
    
    this.start();
};
startMove.prototype.init.prototype = startMove.prototype;

