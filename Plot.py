import matplotlib.pyplot as plt
import numpy as np

def main():
	
	############## Subplot 4 #############
	# np.random.seed(43)
	# data = np.random.normal(0,1,(2,100))
	# x = data[0]
	# y = data[1]

	# fig_mul = plt.figure(figsize=(15,10))

	# # plot 1
	# ax1 = fig_mul.add_subplot(221)
	# ax1.plot(x, y)
	# ax1.set_title('plot 1')
	# ax1.grid(True)
	# ax1.set_xlabel('x')
	# ax1.set_ylabel('y')
	# # plot 2
	# ax2 = fig_mul.add_subplot(222)
	# ax2.plot(x, y)
	# ax2.set_title('plot 2')
	# ax2.grid(False)
	# # plot 3
	# ax3 = fig_mul.add_subplot(223)
	# ax3.plot(x, y)
	# ax3.set_title('plot 3')
	# ax3.grid(False)
	# # plot 4
	# ax4 = fig_mul.add_subplot(224)
	# ax4.plot(x, y)
	# ax4.set_title('plot 4')
	# ax4.grid(False)

	# plt.show()


	############## Graph #############
	# fig = plt.figure(figsize=(10,8))
	# x = np.linspace(0,9,10)
	# x1 = np.random.randint(9, size=30)
	# y1 = x1 + np.random.randn(30)
	# y2 = x + np.random.randn(10)
	# plt.plot(x)
	# plt.plot(x1, y1, 'rs', label='red square')
	# plt.plot(x, y2, 'bs', label='blue square')
	# plt.ylabel('y axis')
	# plt.xlabel('x axis')
	# plt.suptitle('The Graph')
	# plt.legend()

	# # Text
	# # font_dict={'family': 'serif', 
	# #            'color': 'darkred', 
	# #            'size': 15}
	# # plt.text(7, 7, "The content", fontdict=font_dict)

	# plt.annotate('Line of equality', xy=(6.5,6.5), xytext=(0.8, 0.9), textcoords='axes fraction',
	#              arrowprops=dict(arrowstyle="->"),
	#              )
	# plt.show()

if __name__ == "__main__":
	main()