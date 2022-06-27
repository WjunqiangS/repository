package Priv.wangjunqiang.config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;

@ComponentScan("Priv.wangjunqiang.controller")
// 功能之一：开启获取json对象转化为java对象
@EnableWebMvc
public class SpringMVCConfig {
}
