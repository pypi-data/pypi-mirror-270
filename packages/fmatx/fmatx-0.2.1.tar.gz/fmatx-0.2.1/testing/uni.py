__all__ = [
	'gt',
	'gprint',
	'getOptimizationProblem',
]

from os import write as osWt
from time import perf_counter
from sys import stdout

class gt(object) :
	__slots__ = (
		'__t_s',
		'__tag',
		'__lp',
	)
	
	def __init__(self, tag=None, loop=1) :
		self.__tag, self.__lp = \
			('GET TIME' if tag is None else tag), loop
		
	def __call__(self, *args, **kwds) :
		sloop, func = self.__lp>1, self.__tag
		try :
			self.__t_s = perf_counter()
			res = func(*args, **kwds)
		except :
			self.__t_s = perf_counter() - self.__t_s
			try : n = self.__tag.__name__
			except : n = self.__tag
			gt.putout('%s: %.9fs' % (n, self.__t_s))
			raise
		if sloop :
			for _ in range(self.__lp-1) :
				func(*args, **kwds)
		self.__t_s = perf_counter() - self.__t_s
		try : n = self.__tag.__name__
		except : n = self.__tag
		gt.putout('%s: %.9fs' % (n, self.__t_s))
		return res

	def __enter__(self) :
		gt.putout('↓%s↓' % self.__tag)
		self.__t_s = perf_counter()
		return self.__tag
	
	def __exit__(self, exc_type, exc_val, exc_tb) :
		self.__t_s = perf_counter() - self.__t_s
		if self.__lp != 1 :
			raise NotImplemented
		if exc_type is None :
			gt.putout('↑%s→ %.9fs' % (self.__tag, self.__t_s))
		else :
			gt.putout('↑%s→ ERROR' % self.__tag)
		return False
	
	@classmethod
	def putout(cls, *objs, sep=' ', end='\n', flush=False, func=str) :
		osWt(1, sep.join(map(func, objs)).encode()+end.encode())
		if flush : stdout.flush()
	
	@classmethod
	def seeup(cls, obj, end='\n', flush=False, func=str) :
		osWt(1, func(obj).encode()+end.encode())
		if flush : stdout.flush()
		return obj
	
	gt = lambda self : perf_counter() - self.__t_s
	
	def reset(self) :
		self.__t_s = perf_counter()
		
	__name__ = \
		property(lambda s :
			s.__class__.__name__
			if type(s.__tag) in (None, str)
			else s.__tag.__name__)

gprint = gt.putout

def getOptimizationProblem(C, A, b, maximize=False, ILP=False) :
		g = 'max z = ' if maximize else 'min z = '
		SubscriptDict = {i: j for i, j in zip('0123456789.', '₀₁₂₃₄₅₆₇₈₉⡀')}
		toSubscript, checkCoe = (
			lambda n : ''.join(SubscriptDict[i] for i in str(n)),
			lambda n : '' if n == 1 else '-' if n == -1 else n)
		
		f = '+ '.join(f'{checkCoe(j)}x{toSubscript(i)}' for i,j in enumerate(C, 1))
		c = 's.t.\t' + \
			'\n\t\t'.join(
			'+ '.join(f'{checkCoe(u)}x{toSubscript(k)}' for k,u in enumerate(i, 1) if u)\
			+ f' ≤ {j}' for i,j in zip(A.tolist(), b))
		r = 'xₙ ∈ Integers ∧ '*int(ILP) + 'xₙ ≥ 0'
		
		return g + f'{f}\n{c}\n\t\t{r}\n'.replace('+ -', '- ')