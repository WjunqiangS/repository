/**
 * 单例设计模式：让对象在内存中只有一份
 * 单例设计模式的步骤：
 *						1.私有化构造函数
 *						2.在类中创建一个指向本类的私有化引用变量
 *						3.提供一个获取本类对象的公共静态方法
 *
 */
 class Single {
	/** 在类中创建一个指向本类的私有化引用变量 */
	private static Single s = new Single();

	/** 私有化构造函数 */
	private Single() {

	}
 						
	/** 提供一个获取本类对象的公共静态方法 */
	public static Single getInstance() {
		return s;
	}

 }

class SingleDesign 
{
	public static void main(String[] args) 
	{
		Single s = Single.getInstance();
	}
}
