package Priv.wangjunqiang.domain;

import com.baomidou.mybatisplus.annotation.*;
import lombok.Data;

@Data
// 指定数据库表名
// 在全局配置中配置
// @TableName("tbl_book")
public class Book {
    // 在全局配置中配置
    // @TableId(type = IdType.AUTO)
    private long id;
    // 设置数据库字段与变量绑定
    @TableField(value = "type")
    private String type;
    private String name;
    private String description;
    // 设置类属性不在数据库中
    // select可以设置类属性不参与数据库查询
    @TableField(exist = false)
    private String sell;

    // 逻辑删除操作,并不是真正把数据库中的数据删除
    // 在总的配置文件中配置
    // @TableLogic(value = "0", delval = "1")
    private Integer deleted;

    // 处理并发业务，添加乐观锁
    @Version
    private Integer version;
}
