'use client'
import clsx from 'clsx';

type Props = React.ButtonHTMLAttributes<HTMLButtonElement>

export const ARButton = ({ className, ...rest }: Props) => {
    return (
        <button className={clsx(
            'bg-pink-400 text-black-300',
            'py-2 px-4 leading-6',
            'rounded-full',
            'font-semibold tracking-wide',
            'cursor-pointer',
            'inline-flex items-center justify-center',
            'relative shadow',

            'transition',
            'hover:bg-pink-300 hover:shadow-md',

            'outline-none',
            'ring-pink-300/70 ring-offset-2',
            'focus-visible:ring-2 focus:scale-[0.98]',

            className
        )}
            {...rest}
        />
    )
}